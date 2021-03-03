from django.db import models

from simpl.core.managers import ActiveQuerySet


class RoomQuerySet(ActiveQuerySet):
    pass


class RoomManager(models.Manager):

    def get_queryset(self):
        return RoomQuerySet(self.model, using=self._db)
