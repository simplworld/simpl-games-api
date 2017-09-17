from django_filters import rest_framework as filters

from .. import models


class RoleFilter(filters.FilterSet):

    game_slug = filters.CharFilter(name='game__slug')

    class Meta:
        model = models.Role
        fields = [
            'game',
            'name',
            'game_slug',
        ]


class PhaseFilter(filters.FilterSet):

    game_slug = filters.CharFilter(name='game__slug')

    class Meta:
        model = models.Phase
        fields = [
            'game',
            'name',
            'game_slug',
        ]


class RunFilter(filters.FilterSet):

    game_slug = filters.CharFilter(name='game__slug')

    class Meta:
        model = models.Run
        fields = [
            'game',
            'name',
            'game_slug',
        ]


class RunUserFilter(filters.FilterSet):

    game_slug = filters.CharFilter(name='run__game__slug')

    class Meta:
        model = models.RunUser
        fields = [
            'active',
            'leader',
            'role',
            'run',
            'user',
            'world',
            'game_slug',
        ]


class WorldFilter(filters.FilterSet):

    game_slug = filters.CharFilter(name='run__game__slug')

    class Meta:
        model = models.World
        fields = [
            'run',
            'name',
            'game_slug',
        ]


class ScenarioFilter(filters.FilterSet):

    game_slug = filters.CharFilter(name='world__run__game__slug')

    class Meta:
        model = models.Scenario
        fields = [
            'runuser',
            'world',
            'name',
            'game_slug',
        ]


class PeriodFilter(filters.FilterSet):

    game_slug = filters.CharFilter(name='scenario__world__run__game__slug')

    class Meta:
        model = models.Period
        fields = [
            'scenario',
            'order',
            'game_slug',
        ]


class DecisionFilter(filters.FilterSet):

    game_slug = filters.CharFilter(name='period__scenario__world__run__game__slug')

    class Meta:
        model = models.Decision
        fields = [
            'name',
            'period',
            'role',
            'game_slug',
        ]


class ResultFilter(filters.FilterSet):

    game_slug = filters.CharFilter(name='period__scenario__world__run__game__slug')

    class Meta:
        model = models.Result
        fields = [
            'name',
            'period',
            'role',
            'game_slug',
        ]
