import logging
from rest_framework import filters, viewsets, generics
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication
)
from rest_framework.permissions import IsAuthenticated

from rest_framework_bulk.mixins import (
    BulkCreateModelMixin,
    BulkDestroyModelMixin
)

logger = logging.getLogger(__name__)

from . import bulk_serializers, filters
from .. import models


# Mixins supporting bulk create and destroy requests, but not updates

class BulkCreateDestroyModelViewSet(BulkCreateModelMixin,
                                    BulkDestroyModelMixin,
                                    viewsets.ModelViewSet):
    def allow_bulk_destroy(self, qs, filtered_qs):
        # require the qs to be filtered
        # qs comes from self.get_queryset()
        # filtered_qs comes from self.filter_queryset(qs)
        # however, these arguments test not equal so
        # require bulk_destroy requests be filtered by query_params
        return len(self.request.query_params.keys()) > 0


class BulkCommonViewSet(BulkCreateDestroyModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


# Bulk ViewSets

class BulkDecisionViewSet(BulkCommonViewSet):
    """ Decision resource. """
    model = models.Decision
    queryset = models.Decision.objects.all()
    serializer_class = bulk_serializers.BulkDecisionSerializer
    filter_class = filters.DecisionFilter
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add new Decisions
        """
        return super(BulkDecisionViewSet, self).create(request)

    def destroy(self, request):
        """
        Delete filtered Decisions
        """
        return super(BulkDecisionViewSet, self).bulk_destroy(request)


class BulkPeriodViewSet(BulkCommonViewSet):
    """ Period resource. """
    model = models.Period
    queryset = models.Period.objects.all()
    serializer_class = bulk_serializers.BulkPeriodSerializer
    filter_class = filters.PeriodFilter
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add new Periods
        """
        return super(BulkPeriodViewSet, self).create(request)

    def destroy(self, request):
        """
        Delete filtered Periods
        """
        return super(BulkPeriodViewSet, self).bulk_destroy(request)


class BulkPhaseViewSet(BulkCommonViewSet):
    """ Phase resource. """
    model = models.Phase
    queryset = models.Phase.objects.all()
    serializer_class = bulk_serializers.BulkPhaseSerializer
    filter_class = filters.PhaseFilter
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add new Phases
        """
        return super(BulkPhaseViewSet, self).create(request)

    def destroy(self, request):
        """
        Delete filtered Phases
        """
        return super(BulkPhaseViewSet, self).bulk_destroy(request)


class BulkResultViewSet(BulkCommonViewSet):
    """ Result resource. """
    model = models.Result
    queryset = models.Result.objects.all()
    serializer_class = bulk_serializers.BulkResultSerializer
    filter_class = filters.ResultFilter
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add new Results
        """
        return super(BulkResultViewSet, self).create(request)

    def destroy(self, request):
        """
        Delete filtered Results
        """
        return super(BulkResultViewSet, self).bulk_destroy(request)


class BulkRoleViewSet(BulkCommonViewSet):
    """ Role resource. """
    model = models.Role
    queryset = models.Role.objects.all()
    serializer_class = bulk_serializers.BulkRoleSerializer
    filter_class = filters.RoleFilter
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add new Roles
        """
        return super(BulkRoleViewSet, self).create(request)

    def destroy(self, request):
        """
        Delete filtered Role
        """
        return super(BulkRoleViewSet, self).bulk_destroy(request)


class BulkRunViewSet(BulkCommonViewSet):
    """ Run resource. """
    model = models.Run
    queryset = models.Run.objects.all()
    serializer_class = bulk_serializers.BulkRunSerializer
    filter_class = filters.RunFilter
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add new Runs
        """
        return super(BulkRunViewSet, self).create(request)

    def destroy(self, request):
        """
        Delete filtered Runs
        """
        return super(BulkRunViewSet, self).bulk_destroy(request)


class BulkRunUserViewSet(BulkCommonViewSet):
    """ RunUser resource. """
    model = models.RunUser
    queryset = \
        models.RunUser.objects.select_related('user', 'run__game', 'role')
    serializer_class = bulk_serializers.BulkRunUserSerializer
    filter_class = filters.RunUserFilter
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add new RunUsers
        """
        return super(BulkRunUserViewSet, self).create(request)

    def destroy(self, request):
        """
        Delete filtered RunUsers
        """
        return super(BulkRunUserViewSet, self).bulk_destroy(request)


class BulkScenarioViewSet(BulkCommonViewSet):
    """ Scenario resource. """
    model = models.Scenario
    queryset = models.Scenario.objects.all()
    serializer_class = bulk_serializers.BulkScenarioSerializer
    filter_class = filters.ScenarioFilter
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add new Scenario
        """
        return super(BulkScenarioViewSet, self).create(request)

    def destroy(self, request):
        """
        Delete filtered Scenarios
        """
        return super(BulkScenarioViewSet, self).bulk_destroy(request)


class BulkWorldViewSet(BulkCommonViewSet):
    """ World resource. """
    model = models.World
    queryset = models.World.objects.all()
    serializer_class = bulk_serializers.BulkWorldSerializer
    filter_class = filters.WorldFilter
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add new Worlds
        """
        return super(BulkWorldViewSet, self).create(request)

    def destroy(self, request):
        """
        Delete filtered Worlds
        """
        return super(BulkWorldViewSet, self).bulk_destroy(request)
