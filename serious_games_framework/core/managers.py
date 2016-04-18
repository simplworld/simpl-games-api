from django.db import models


class ActiveQuerySet(models.QuerySet):

    def active(self):
        return self.filter(active__exact=True)

    def inactive(self):
        return self.filter(active__exact=False)
