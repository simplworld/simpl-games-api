import requests

from django.apps import apps
from django.utils import timezone
from celery import shared_task


@shared_task
def send_webhook(event, url, payload, connected, erroring, subscriber_id):
    """
    Send a HTTP POST (webhook) with the payload to the subscribed URL.

    We are also passed whether or not this subscriber has been connected
    before, whether or not they have been erroring lately and the subscriber_id.

    We use these to determine if we need to retrieve the subscriber object
    from the database and update the status.  So for example, if they're
    already showing they are connected we don't need to update that except for
    the first successful connection.

    In the case of errors, we want to update the database when we see a
    successful webhook happen.  To avoid blocking non-erroring tasks we assume
    the dispatch call for this task sets a small ETA countdown on the Celery
    task to help ensure erroring tasks do not clog the Celery broker's queue.
    """
    Subscriber = apps.get_model('webhooks', 'Subscriber')

    try:
        res = requests.post(
            url=url,
            headers={'Content-type': 'application/json'},
            data=payload,
        ).raise_for_status()
    except requests.exceptions.RequestException:
        # Handle recording errors
        sub = Subscriber.objects.get(pk=subscriber_id)
        sub.erroring = True
        sub.last_error = timezone.now()
        sub.last_error_status = res.status_code
        sub.last_error_content = res.content
        sub.save()

        # Reraise the exception so Celery see this as a failed task
        raise

    # Record if this is our first successful connection for this subscriber
    if not connected:
        sub = Subscriber.objects.get(pk=subscriber_id)
        sub.connected = True
        sub.save()
