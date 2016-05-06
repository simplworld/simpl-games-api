from django.db import models


class ActiveQuerySet(models.QuerySet):

    def active(self):
        """Return a list of active objects"""

        return self.filter(active__exact=True)

    def inactive(self):
        """Return a list of inactive objects"""

        return self.filter(active__exact=False)
