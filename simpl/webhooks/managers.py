from django.db import models
from django.conf import settings


class SubscriberQuerySet(models.QuerySet):

    def erroring(self):
        return self.filter(connected=True, erroring=True)

    def not_connected(self):
        return self.filter(connected=False)

    def connected(self):
        return self.filter(connected=True)


class SubscriberManager(models.Manager):

    def get_queryset(self):
        return SubscriberQuerySet(self.model, using=self._db)

    def _check_url(self, url):
        """ Determine if our URL is ok """
        allow_localhost = getattr(settings, "SIMPL_WEBHOOKS_ALLOW_LOCALHOST", False)

        if not allow_localhost and 'localhost' in url:
            raise ValueError("Simpl is not configured to allow localhost URLs")

        allow_http = getattr(settings, "SIMPL_WEBHOOKS_ALLOW_HTTP", False)

        if not allow_http and 'https' not in url:
            raise ValueError("Simpl is not configured to allow non-HTTPS urls")

        return url

    def create_subscription(self, event, user, url):
        """ Create subscriptions checking our safety setting """
        url = self._check_url(url)
        sub = self.create(event=event, user=user, url=url)
        # FIXME log creation
        return sub

    def erroring(self):
        return self.get_queryset().erroring()

    def not_connected(self):
        return self.get_queryset().not_connected()

    def connected(self):
        return self.get_queryset().connected()