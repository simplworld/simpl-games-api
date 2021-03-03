from django.core.exceptions import ValidationError
from django.core.validators import validate_email, validate_slug

from .exceptions import MessageValidationError

REQUIRED_MESSAGE_KEYS = [
    "room",
    "sender",
    "message",
    "created",
]


def validate_message(message):
    """
    Messages need to have a very specific keys of certain data types but
    extra keys are allowed so Simpl developers can extend from a basic
    text message.

    The keys that are required are:
    {
        "room": "<room-slug>",
        "sender": "<sender@email.com>",
        "message": "Strong representation of the message",
        "created": "Timestamp when message was created",
    }

    As an example, if you wanted to make a richer Message type you could
    certainly add some extra keys and adjust your frontend code to handle the
    display of them.  Some ideas of extra keys that could happen in a game:

    - gender
    - team
    - role
    - image_url
    """

    # Check that the keys even exist
    for key in REQUIRED_MESSAGE_KEYS:
        if key not in message:
            raise MessageValidationError(f"'{key}' is missing from Message")

    # Ensure sender looks like an email address
    try:
        validate_email(message["sender"])
    except ValidationError:
        raise MessageValidationError("'sender' is not a valid email address")

    # Ensure room looks like a slug
    try:
        validate_slug(message["room"])
    except ValidationError:
        raise MessageValidationError("'room' is not a valid slug")

    # Ensure message has something in it
    if message["message"] is None:
        raise MessageValidationError("'message' key must contain some text representation of the message")

    return True
