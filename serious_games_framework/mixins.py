from django.db import models
from django.utils import timezone


# Abstract Mixins

class AbstractTimeStampedModel(models.Model):
    """
    Basic audit fields that every model should have.
    """
    created = models.DateTimeField(
        default=timezone.now, blank=True, db_index=True
    )
    updated = models.DateTimeField(blank=True)

    def save(self, **kwargs):
        self.updated = timezone.now()
        return super(AbstractTimeStampedModel, self).save(**kwargs)

    class Meta:
        abstract = True
