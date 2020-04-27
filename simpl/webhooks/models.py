from django.conf import settings
from django.db import models
from django.utils import timezone

from .managers import SubscriberManager


class Subscriber(models.Model):
    """
    Model to track webhook subscribers
    """
    event = models.CharField(max_length=200, db_index=True, help_text="Events to receive, should be namespaced with periods 'user.*', 'blackjack.*', etc.")
    url = models.URLField(max_length=255, db_index=True, help_text="URL to POST event")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="webhook_subscriptions", on_delete=models.CASCADE)

    connected = models.BooleanField(db_index=True, default=False, help_text="Has sent successful hooks in the past")
    erroring = models.BooleanField(db_index=True, default=False, help_text="Currently erroring out")

    last_error = models.DateTimeField(blank=True, null=True, help_text="Last webhook POST that errored")
    last_error_status = models.IntegerField(blank=True, null=True)
    last_error_content = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    objects = SubscriberManager()

    def __str__(self):
        return f"'{self.event}' -> {self.url} ({self.user})"

    def record_error(self, status, content):
        """ Record an error sending to this URL """
        self.erroring = True
        self.last_error = timezone.now()

        try:
            self.last_error_status = int(status)
            self.last_error_content = content
        except ValueError:
            self.last_error_status = None
            self.last_error_content = f"INVALID STATUS '{status}': {content}"

        self.save()

    def clear_error(self):
        """ Clear previous error, which assumes connection """
        if self.erroring:
            self.erroring = False
            self.connected = True
            self.save()

    def record_connect(self):
        """ Record a successful connection """
        if not self.connected:
            self.connected = True
            self.save()
