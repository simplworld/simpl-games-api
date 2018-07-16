from django_filters import rest_framework as filters
from django.db.models import Q

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
            'active',
        ]


class RunUserFilter(filters.FilterSet):
    game_slug = filters.CharFilter(name='run__game__slug')
    run_active = filters.BooleanFilter(name='run__active')

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
            'run_active',
        ]


class WorldFilter(filters.FilterSet):
    game_slug = filters.CharFilter(name='run__game__slug')
    run_active = filters.BooleanFilter(name='run__active')

    class Meta:
        model = models.World
        fields = [
            'run',
            'name',
            'game_slug',
            'run_active',
        ]


class ScenarioFilter(filters.FilterSet):
    game_slug = filters.CharFilter(name='special-filter',
                                   method='filter_runuser_and_worlds_in_game')

    def filter_runuser_and_worlds_in_game(self, queryset, name, value):
        """
        We need to retrieve Scenarios which are attached to worlds or runusers
        in the given game slug
        """
        return queryset.filter(
            Q(world__run__game__slug=value) |
            Q(runuser__run__game__slug=value)
        )

    run_active = filters.BooleanFilter(name='special-filter',
                                       method='filter_runuser_and_worlds_in_run_active')

    def filter_runuser_and_worlds_in_run_active(self, queryset, name, value):
        """
        We need to retrieve Scenarios which are attached to worlds or runusers
        in runs with active value
        """
        return queryset.filter(
            Q(world__run__active=value) |
            Q(runuser__run__active=value)
        )

    class Meta:
        model = models.Scenario
        fields = [
            'runuser',
            'world',
            'name',
            'game_slug',
            'run_active',
            'world__run',
            'runuser__run',
        ]


class PeriodFilter(filters.FilterSet):
    game_slug = filters.CharFilter(name='special-filter',
                                   method='filter_runuser_and_worlds_in_game')

    def filter_runuser_and_worlds_in_game(self, queryset, name, value):
        """
        We need to retrieve Periods in Scenarios which are attached to worlds
        or runusers in the given game slug
        """
        return queryset.filter(
            Q(scenario__world__run__game__slug=value) |
            Q(scenario__runuser__run__game__slug=value)
        )

    run_active = filters.BooleanFilter(name='special-filter',
                                       method='filter_runuser_and_worlds_in_run_active')

    def filter_runuser_and_worlds_in_run_active(self, queryset, name, value):
        """
        We need to retrieve Periods in Scenarios  which are attached to worlds
        or runusers in runs with active value
        """
        return queryset.filter(
            Q(scenario__world__run__active=value) |
            Q(scenario__runuser__run__active=value)
        )

    class Meta:
        model = models.Period
        fields = [
            'scenario',
            'order',
            'game_slug',
            'run_active',
            'scenario__world__run',
            'scenario__runuser__run'
        ]


class DecisionFilter(filters.FilterSet):
    game_slug = filters.CharFilter(name='special-filter',
                                   method='filter_runuser_and_worlds_in_game')

    def filter_runuser_and_worlds_in_game(self, queryset, name, value):
        """
        We need to retrieve Decisions attached to Periods in Scenarios which are
        attached to worlds or runusers in the given game slug
        """
        return queryset.filter(
            Q(period__scenario__world__run__game__slug=value) |
            Q(period__scenario__runuser__run__game__slug=value)
        )

    run_active = filters.BooleanFilter(name='special-filter',
                                       method='filter_runuser_and_worlds_in_run_active')

    def filter_runuser_and_worlds_in_run_active(self, queryset, name, value):
        """
        We need to retrieve Decisions attached to Periods in Scenarios which are
        attached to worlds or runusers in runs with active value
        """
        return queryset.filter(
            Q(period__scenario__world__run__active=value) |
            Q(period__scenario__runuser__run__active=value)
        )

    class Meta:
        model = models.Decision
        fields = [
            'name',
            'period',
            'role',
            'game_slug',
            'run_active',
            'period__scenario__world__run',
            'period__scenario__runuser__run'
        ]


class ResultFilter(filters.FilterSet):
    game_slug = filters.CharFilter(name='special-filter',
                                   method='filter_runuser_and_worlds_in_game')

    def filter_runuser_and_worlds_in_game(self, queryset, name, value):
        """
        We need to retrieve Results attached to Periods in Scenarios which are
        attached to worlds or runusers in the given game slug
        """
        return queryset.filter(
            Q(period__scenario__world__run__game__slug=value) |
            Q(period__scenario__runuser__run__game__slug=value)
        )

    run_active = filters.BooleanFilter(name='special-filter',
                                       method='filter_runuser_and_worlds_in_run_active')

    def filter_runuser_and_worlds_in_run_active(self, queryset, name, value):
        """
        We need to retrieve Results attached to Periods in Scenarios which are
        attached to worlds or runusers in runs with active value
        """
        return queryset.filter(
            Q(period__scenario__world__run__active=value) |
            Q(period__scenario__runuser__run__active=value)
        )

    class Meta:
        model = models.Result
        fields = [
            'name',
            'period',
            'role',
            'game_slug',
            'run_active',
            'period__scenario__world__run',
            'period__scenario__runuser__run'
        ]
