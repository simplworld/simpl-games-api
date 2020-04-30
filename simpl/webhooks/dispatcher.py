import requests
import uuid

from django.conf import settings
from django.core.cache import cache
from .models import Subscriber
from .tasks import send_webhook

SIMPL_WEBHOOKS_SUBSCRIBER_CACHE_TIMEOUT = getattr(settings, "SIMPL_WEBHOOKS_SUBSCRIBER_CACHE_TIMEOUT", 300)


class Dispatcher:
    """
    Handle dispatching webhooks via Celery or into a local array to inspect
    for testing purposes
    """

    def get_subscribers(self, event_name):
        """ Retrieve subscribers for an event """
        cache_key = f"simpl:{event_name}"

        subscribers = cache.get(cache_key, None)
        if subscribers is None:
            subscribers = list(Subscriber.objects.by_event(event_name))

            cache.set(cache_key, subscribers, SIMPL_WEBHOOKS_SUBSCRIBER_CACHE_TIMEOUT)

        return subscribers

    def send(self, event, data):
        """
        Send a payload to a subscriber. This is builds the full payload
        """
        # Build our payload
        payload = {
            "event": event,
            "ref": str(uuid.uuid4()),
            "data": data
        }

        subscribers = self.get_subscribers(event)

        # Send to each subscriber
        [self.send_to_subscriber(event, sub, payload) for sub in subscribers]

    def send_to_subscriber(self, event, subscriber, data):
        """
        Send the data to the subscriber.  We need to pass along if the
        subscriber is erroring and/or connected so the Celery task does not
        bother to hit the database for an update.

        We will also delay erroring subscribers a bit into the future to allow
        non-erroring subscribers to move to the front of the queue
        """
        # Default to send the task immediately
        countdown = 0

        if subscriber.erroring:
            countdown = 5

        send_webhook.apply_async(
            (event, subscriber.url, data, subscriber.connected, subscriber.erroring, subscriber.id),
            countdown=countdown)
