import logging

from rest_framework import filters, viewsets
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from .. import models

logger = logging.getLogger(__name__)


# Mixins

class CommonViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


# ViewSets

class DecisionViewSet(CommonViewSet):
    """ Decision resource. """

    queryset = models.Decision.objects.all()
    serializer_class = serializers.DecisionSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        'period',
        'role',
        'name',
    )
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add a new Decision
        """
        return super(DecisionViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        Delete an Decision
        """
        return super(DecisionViewSet, self).destroy(request, pk=pk)

    def list(self, request):
        """
        Returns a list of Decisions
        ---
        parameters:
            - name: name
              type: string
              paramType: query
              required: false
              description: Filters Decisions per Name via name
            - name: period
              type: integer
              paramType: query
              required: false
              description: Filters Decisions per Period via period
            - name: role
              type: integer
              paramType: query
              required: false
              description: Filters Decisions per Role via role
        """
        return super(DecisionViewSet, self).list(request)

    def partial_update(self, request, pk=None):
        """
        Update an existing Decision
        """
        return super(DecisionViewSet, self).partial_update(request, pk=pk)

    def retrieve(self, request, pk=None):
        """
        Find an Decision by ID
        """
        return super(DecisionViewSet, self).retrieve(request, pk=pk)

    def update(self, request, pk=None):
        """
        Update an existing Decision
        """
        return super(DecisionViewSet, self).update(request, pk=pk)


class GameViewSet(CommonViewSet):
    """ Game resource. """

    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        'active',
        'name',
        'slug',
    )
    lookup_field = 'slug'
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add a new Game
        """
        return super(GameViewSet, self).create(request)

    def destroy(self, request, slug=None):
        """
        Delete an Game
        """
        return super(GameViewSet, self).destroy(request, slug=slug)

    def list(self, request):
        """
        Returns a list of Games
        ---
        parameters:
            - name: active
              type: boolean
              paramType: query
              required: false
              description: Filters Games per Active via active
            - name: name
              type: string
              paramType: query
              required: false
              description: Filters Games per Name via name
            - name: slug
              type: string
              paramType: query
              required: false
              description: Filters Games per Slug via slug
        """
        return super(GameViewSet, self).list(request)

    def partial_update(self, request, slug=None):
        """
        Update an existing Game
        """
        return super(GameViewSet, self).partial_update(request, slug=slug)

    def retrieve(self, request, slug=None):
        """
        Find an Game by ID
        """
        return super(GameViewSet, self).retrieve(request, slug=slug)

    def update(self, request, slug=None):
        """
        Update an existing Game
        """
        return super(GameViewSet, self).update(request, slug=slug)


class PeriodViewSet(CommonViewSet):
    """ Period resource. """

    queryset = models.Period.objects.all()
    serializer_class = serializers.PeriodSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        'scenario',
        'order',
    )
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add a new Period
        """
        return super(PeriodViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        Delete an Period
        """
        return super(PeriodViewSet, self).destroy(request, pk=pk)

    def list(self, request):
        """
        Returns a list of Periods
        ---
        parameters:
            - name: name
              type: string
              paramType: query
              required: false
              description: Filters Periods per Name via name
            - name: scenario
              type: integer
              paramType: query
              required: false
              description: Filters Periods per Scenario via scenario
        """
        return super(PeriodViewSet, self).list(request)

    def partial_update(self, request, pk=None):
        """
        Update an existing Period
        """
        return super(PeriodViewSet, self).partial_update(request, pk=pk)

    def retrieve(self, request, pk=None):
        """
        Find an Period by ID
        """
        return super(PeriodViewSet, self).retrieve(request, pk=pk)

    def update(self, request, pk=None):
        """
        Update an existing Period
        """
        return super(PeriodViewSet, self).update(request, pk=pk)


class PhaseViewSet(CommonViewSet):
    """ Phase resource. """

    queryset = models.Phase.objects.all()
    serializer_class = serializers.PhaseSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        'game',
        'name',
    )
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add a new Phase
        """
        return super(PhaseViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        Delete an Phase
        """
        return super(PhaseViewSet, self).destroy(request, pk=pk)

    def list(self, request):
        """
        Returns a list of Phases
        ---
        parameters:
            - name: game
              type: integer
              paramType: query
              required: false
              description: Filters Phases per Game via game
            - name: name
              type: string
              paramType: query
              required: false
              description: Filters Phases per Name via name
        """
        return super(PhaseViewSet, self).list(request)

    def partial_update(self, request, pk=None):
        """
        Update an existing Phase
        """
        return super(PhaseViewSet, self).partial_update(request, pk=pk)

    def retrieve(self, request, pk=None):
        """
        Find an Phase by ID
        """
        return super(PhaseViewSet, self).retrieve(request, pk=pk)

    def update(self, request, pk=None):
        """
        Update an existing Phase
        """
        return super(PhaseViewSet, self).update(request, pk=pk)


class ResultViewSet(CommonViewSet):
    """ Result resource. """

    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        'period',
        'role',
        'name',
    )
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add a new Result
        """
        return super(ResultViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        Delete an Result
        """
        return super(ResultViewSet, self).destroy(request, pk=pk)

    def list(self, request):
        """
        Returns a list of Results
        ---
        parameters:
            - name: name
              type: string
              paramType: query
              required: false
              description: Filters Results per Name via name
            - name: period
              type: integer
              paramType: query
              required: false
              description: Filters Results per Period via period
            - name: role
              type: integer
              paramType: query
              required: false
              description: Filters Results per Role via role
        """
        return super(ResultViewSet, self).list(request)

    def partial_update(self, request, pk=None):
        """
        Update an existing Result
        """
        return super(ResultViewSet, self).partial_update(request, pk=pk)

    def retrieve(self, request, pk=None):
        """
        Find an Result by ID
        """
        return super(ResultViewSet, self).retrieve(request, pk=pk)

    def update(self, request, pk=None):
        """
        Update an existing Result
        """
        return super(ResultViewSet, self).update(request, pk=pk)


class RoleViewSet(CommonViewSet):
    """ Role resource. """

    queryset = models.Role.objects.all()
    serializer_class = serializers.RoleSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        'game',
        'name',
    )
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add a new Role
        """
        return super(RoleViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        Delete an Role
        """
        return super(RoleViewSet, self).destroy(request, pk=pk)

    def list(self, request):
        """
        Returns a list of Roles
        ---
        parameters:
            - name: game
              type: integer
              paramType: query
              required: false
              description: Filters Roles per Game via game
            - name: name
              type: string
              paramType: query
              required: false
              description: Filters Roles per Name via name
        """
        return super(RoleViewSet, self).list(request)

    def partial_update(self, request, pk=None):
        """
        Update an existing Role
        """
        return super(RoleViewSet, self).partial_update(request, pk=pk)

    def retrieve(self, request, pk=None):
        """
        Find an Role by ID
        """
        return super(RoleViewSet, self).retrieve(request, pk=pk)

    def update(self, request, pk=None):
        """
        Update an existing Role
        """
        return super(RoleViewSet, self).update(request, pk=pk)


class RunViewSet(CommonViewSet):
    """ Run resource. """

    queryset = models.Run.objects.all()
    serializer_class = serializers.RunSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        'game',
        'name',
        'phase',
    )
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add a new Run
        """
        return super(RunViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        Delete an Run
        """
        return super(RunViewSet, self).destroy(request, pk=pk)

    def list(self, request):
        """
        Returns a list of Runs
        ---
        parameters:
            - name: game
              type: integer
              paramType: query
              required: false
              description: Filters Runs per Game via game
            - name: name
              type: string
              paramType: query
              required: false
              description: Filters Runs per Name via name
        """
        return super(RunViewSet, self).list(request)

    def partial_update(self, request, pk=None):
        """
        Update an existing Run
        """
        return super(RunViewSet, self).partial_update(request, pk=pk)

    def retrieve(self, request, pk=None):
        """
        Find an Run by ID
        """
        return super(RunViewSet, self).retrieve(request, pk=pk)

    def update(self, request, pk=None):
        """
        Update an existing Run
        """
        return super(RunViewSet, self).update(request, pk=pk)


class RunUserViewSet(CommonViewSet):
    """ RunUser resource. """

    queryset = models.RunUser.objects.select_related('user', 'run__game',
                                                     'role')
    serializer_class = serializers.RunUserSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        'active',
        'leader',
        'role',
        'run',
        'user',
        'world',
    )
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add a new RunUser
        """
        return super(RunUserViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        Delete a RunUser
        """
        return super(RunUserViewSet, self).destroy(request, pk=pk)

    def list(self, request):
        """
        Returns a list of RunUsers
        ---
        parameters:
            - name: active
              type: boolean
              paramType: query
              required: false
              description: Filters RunUsers per Active via active
            - name: leader
              type: boolean
              paramType: query
              required: false
              description: Filters RunUsers per Leader via leader
            - name: role
              type: integer
              paramType: query
              required: false
              description: Filters RunUsers per Role via role
            - name: run
              type: integer
              paramType: query
              required: false
              description: Filters RunUsers per Run via run
            - name: user
              type: integer
              paramType: query
              required: false
              description: Filters RunUsers per User via user
            - name: world
              type: integer
              paramType: query
              required: false
              description: Filters RunUsers per World via world
        """
        return super(RunUserViewSet, self).list(request)

    def partial_update(self, request, pk=None):
        """
        Update an existing RunUser
        """
        return super(RunUserViewSet, self).partial_update(request, pk=pk)

    def retrieve(self, request, pk=None):
        """
        Find an RunUser by ID
        """
        return super(RunUserViewSet, self).retrieve(request, pk=pk)

    def update(self, request, pk=None):
        """
        Update an existing RunUser
        """
        return super(RunUserViewSet, self).update(request, pk=pk)


class ScenarioViewSet(CommonViewSet):
    """ Scenario resource. """

    queryset = models.Scenario.objects.all()
    serializer_class = serializers.ScenarioSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        'runuser',
        'world',
        'name',
    )
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add a new Scenario
        """
        return super(ScenarioViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        Delete an Scenario
        """
        return super(ScenarioViewSet, self).destroy(request, pk=pk)

    def list(self, request):
        """
        Returns a list of Scenarioes
        ---
        parameters:
            - name: name
              type: string
              paramType: query
              required: false
              description: Filters Scenarioes per Name via name
            - name: runuser
              type: integer
              paramType: query
              required: false
              description: Filters Scenarioes per Creator RunUser via runuser
            - name: world
              type: integer
              paramType: query
              required: false
              description: Filters Scenarioes per World via world
              TODO: Not all scenarios are associated with world
        """
        return super(ScenarioViewSet, self).list(request)

    def partial_update(self, request, pk=None):
        """
        Update an existing Scenario
        """
        return super(ScenarioViewSet, self).partial_update(request, pk=pk)

    def retrieve(self, request, pk=None):
        """
        Find an Scenario by ID
        """
        return super(ScenarioViewSet, self).retrieve(request, pk=pk)

    def update(self, request, pk=None):
        """
        Update an existing Scenario
        """
        return super(ScenarioViewSet, self).update(request, pk=pk)

    @detail_route(methods=['post'])
    def rewind(self, request, pk=None):
        """
        Rewind the scenario back to its period with the specified 'last_period_order'
        by deleting all periods whose order is greater than last_period_order.
        By default, the decisions and results of the period with the specified last_period_order are deleted.
        Specify 'last_period_order' in post data to be non-zero to prevent deleting all periods back to period with order=0.
        Specify 'delete_period_decisions' in post data to be False to prevent deleting the period's decisions.
        Specify 'delete_period_results' in post data to be False to prevent deleting the period's results.
        :param request:
        :param pk: scenario id
        :raises models.Period.DoesNotExist if the scenario does not have a period with specified last_period_order
        """
        # logger.debug("scenarios/rewind: request.data: %s", request.data)

        scenario = self.get_object()
        last_period_order = request.data.get('last_period_order', 0)
        delete_last_period_decisions = \
            request.data.get('delete_last_period_decisions', True)
        delete_last_period_results = \
            request.data.get('delete_last_period_results', True)

        # logger.debug("scenarios/rewind: last_period_order: %s", last_period_order)
        # logger.debug("scenarios/rewind: delete_last_period_decisions: %s", delete_last_period_decisions)
        # logger.debug("scenarios/rewind: delete_last_period_results: %s", delete_last_period_results)

        last_period = None
        periods = models.Period.objects.filter(scenario=scenario)
        # logger.debug("scenarios/rewind: periods: %s", periods)
        for period in periods:
            if period.order is last_period_order:
                last_period = period
            elif period.order > last_period_order:
                period.delete()
        if last_period is None:
            logger.error('last_period does not exist')
            raise models.Period.DoesNotExist()

        if delete_last_period_decisions is True:
            # logger.debug("scenarios/rewind: delete last_period decisions")
            decisions = models.Decision.objects.filter(period=last_period)
            for decision in decisions:
                decision.delete()

        if delete_last_period_results is True:
            # logger.debug("scenarios/rewind: delete last_period results")
            results = models.Result.objects.filter(period=last_period)
            for result in results:
                result.delete()

        return Response(None, status.HTTP_204_NO_CONTENT)


class WorldViewSet(CommonViewSet):
    """ World resource. """

    queryset = models.World.objects.all()
    serializer_class = serializers.WorldSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        'run',
        'name',
    )
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add a new World
        """
        return super(WorldViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        Delete an World
        """
        return super(WorldViewSet, self).destroy(request, pk=pk)

    def list(self, request):
        """
        Returns a list of Worlds
        ---
        parameters:
            - name: name
              type: string
              paramType: query
              required: false
              description: Filters Worlds per Name via name
            - name: run
              type: integer
              paramType: query
              required: false
              description: Filters Worlds per Run via run
        """
        return super(WorldViewSet, self).list(request)

    def partial_update(self, request, pk=None):
        """
        Update an existing World
        """
        return super(WorldViewSet, self).partial_update(request, pk=pk)

    def retrieve(self, request, pk=None):
        """
        Find an World by ID
        """
        return super(WorldViewSet, self).retrieve(request, pk=pk)

    def update(self, request, pk=None):
        """
        Update an existing World
        """
        return super(WorldViewSet, self).update(request, pk=pk)
