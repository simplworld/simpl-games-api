import logging

from rest_framework import viewsets
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from . import filters, serializers
from .. import models

logger = logging.getLogger(__name__)


# Mixins

class CommonViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


# ViewSets

class DecisionViewSet(CommonViewSet):
    """ Decision resource. """

    queryset = models.Decision.objects.all().select_related('period')
    serializer_class = serializers.DecisionSerializer
    filterset_class = filters.DecisionFilter
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
            - name: game_slug
              type: string
              paramType: query
              required: false
              description: Filters Decisions per Game via slug
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
    filterset_fields = (
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

    queryset = models.Period.objects.all().select_related('scenario')
    serializer_class = serializers.PeriodSerializer
    filterset_class = filters.PeriodFilter
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
            - name: scenario
              type: integer
              paramType: query
              required: false
              description: Filters Periods per Scenario via scenario
            - name: order
              type: integer
              paramType: query
              required: false
              description: Filters Periods by order
            - name: game_slug
              type: string
              paramType: query
              required: false
              description: Filters Periods per Game via slug
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
    filterset_class = filters.PhaseFilter
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
            - name: game_slug
              type: string
              paramType: query
              required: false
              description: Filters Phases per Game via slug
            - name: slug
              type: string
              paramType: query
              required: false
              description: Filters Phases per Slug via slug
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

    queryset = models.Result.objects.all().select_related('period')
    serializer_class = serializers.ResultSerializer
    filterset_class = filters.ResultFilter
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
            - name: game_slug
              type: string
              paramType: query
              required: false
              description: Filters Results per Game via slug
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
    filterset_class = filters.RoleFilter
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
            - name: game_slug
              type: string
              paramType: query
              required: false
              description: Filters Roles per Game via slug
            - name: slug
              type: string
              paramType: query
              required: false
              description: Filters Roles per Slug via slug
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
    filterset_class = filters.RunFilter
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
            - name: game_slug
              type: string
              paramType: query
              required: false
              description: Filters Runs per Game via slug
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

    queryset = models.RunUser.objects.all().select_related(
        'user', 'run', 'role',
    )
    serializer_class = serializers.RunUserSerializer
    filterset_class = filters.RunUserFilter
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
            - name: game_slug
              type: string
              paramType: query
              required: false
              description: Filters RunUsers per Game via slug
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

    queryset = models.Scenario.objects.all().select_related('runuser',
                                                            'world')
    serializer_class = serializers.ScenarioSerializer
    filterset_class = filters.ScenarioFilter
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
              description: Filters Scenarioes per RunUser via runuser
            - name: world
              type: integer
              paramType: query
              required: false
              description: Filters Scenarioes per World via world
            - name: game_slug
              type: string
              paramType: query
              required: false
              description: Filters Scenarioes per Game via slug
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

    @action(detail=True, methods=['post'])
    def rewind(self, request, pk=None):
        """
        Rewind the scenario back to its period with the specified
        'last_period_order' by deleting all periods whose order is
        greater than last_period_order.
        By default, the decisions and results of the period with
        the specified last_period_order are deleted.
        Specify 'last_period_order' in post data to be non-zero to prevent
        deleting all periods back to period with order=0.
        Specify 'delete_last_period_decisions' in post data to be False to
        prevent deleting the last period's decisions.
        Specify 'delete_last_period_results' in post data to be False to
        prevent deleting the last period's results.
        :param request:
        :param pk: scenario id
        :raises models.Period.DoesNotExist if the scenario does not have
        a period with specified last_period_order
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
        models.Period.objects.filter(scenario=scenario,
                                     order__gt=last_period_order).delete()
        try:
            last_period = models.Period.objects.get(scenario=scenario,
                                                    order=last_period_order)
        except models.Period.DoesNotExist:
            logger.error('last_period does not exist')
            raise

        if delete_last_period_decisions is True:
            # logger.debug("scenarios/rewind: delete last_period decisions")
            models.Decision.objects.filter(period=last_period).delete()

        if delete_last_period_results is True:
            # logger.debug("scenarios/rewind: delete last_period results")
            models.Result.objects.filter(period=last_period).delete()

        return Response(None, status.HTTP_204_NO_CONTENT)


class WorldViewSet(CommonViewSet):
    """ World resource. """

    queryset = models.World.objects.all().select_related('run', )
    serializer_class = serializers.WorldSerializer
    filterset_class = filters.WorldFilter
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
            - name: game_slug
              type: string
              paramType: query
              required: false
              description: Filters Worlds per Game via slug
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
