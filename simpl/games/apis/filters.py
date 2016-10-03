import django_filters

from rest_framework import filters

from .. import models


class WorldFilterSet(filters.FilterSet):
    game_slug = django_filters.CharFilter(name="run__game__slug")

    class Meta:
        model = models.World
        fields = ['game_slug', 'run', 'name']
