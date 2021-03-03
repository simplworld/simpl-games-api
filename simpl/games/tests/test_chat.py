import pytest

from simpl.games.chat import REQUIRED_MESSAGE_KEYS, validate_message
from simpl.games.exceptions import MessageValidationError


def test_required_message_keys():
    # Just leaving this here so it screams at the developer if they try to
    # remove a required key
    assert "room" in REQUIRED_MESSAGE_KEYS
    assert "sender" in REQUIRED_MESSAGE_KEYS
    assert "message" in REQUIRED_MESSAGE_KEYS
    assert "created" in REQUIRED_MESSAGE_KEYS


def test_validate_message():
    # Test a valid message
    valid_message = {
        "room": "some-slug",
        "sender": "frank@revsys.com",
        "message": "This is a test",
        "created": "2020-11-15 16:25:19.022011+00:00",
    }

    assert validate_message(valid_message) is True

    # Message up the message in various ways
    for key in REQUIRED_MESSAGE_KEYS:
        new = valid_message.copy()
        del new[key]

        with pytest.raises(MessageValidationError):
            validate_message(new)

    # Bad email
    new = valid_message.copy()
    new["sender"] = "frank"
    with pytest.raises(MessageValidationError):
        validate_message(new)

    # Bad slug
    new = valid_message.copy()
    new["room"] = "this is a bad slug"
    with pytest.raises(MessageValidationError):
        validate_message(new)

    # Missing message
    new = valid_message.copy()
    new["message"] = None
    with pytest.raises(MessageValidationError):
        validate_message(new)