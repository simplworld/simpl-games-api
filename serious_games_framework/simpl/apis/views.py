from rest_framework import filters, status, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import serializers
from .. import models


# Mixins

class CommonViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    pass


# Views

class DecisionViewSet(CommonViewSet):
    """ Decision resource. """

    queryset = models.Decision.objects.all()
    serializer_class = serializers.DecisionSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        # 'name',
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
        'name',
    )
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add a new Game
        """
        return super(GameViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        Delete an Game
        """
        return super(GameViewSet, self).destroy(request, pk=pk)

    def list(self, request):
        """
        Returns a list of Games
        ---
        parameters:
            - name: name
              type: string
              paramType: query
              required: false
              description: Filters Games per Name via name
        """
        return super(GameViewSet, self).list(request)

    def partial_update(self, request, pk=None):
        """
        Update an existing Game
        """
        return super(GameViewSet, self).partial_update(request, pk=pk)

    def retrieve(self, request, pk=None):
        """
        Find an Game by ID
        """
        return super(GameViewSet, self).retrieve(request, pk=pk)

    def update(self, request, pk=None):
        """
        Update an existing Game
        """
        return super(GameViewSet, self).update(request, pk=pk)


class PeriodViewSet(CommonViewSet):
    """ Period resource. """

    queryset = models.Period.objects.all()
    serializer_class = serializers.PeriodSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        # 'name',
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
        # 'name',
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
        # 'name',
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
        # 'name',
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


class RoundViewSet(CommonViewSet):
    """ Round resource. """

    queryset = models.Round.objects.all()
    serializer_class = serializers.RoundSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        # 'name',
    )
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add a new Round
        """
        return super(RoundViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        Delete an Round
        """
        return super(RoundViewSet, self).destroy(request, pk=pk)

    def list(self, request):
        """
        Returns a list of Rounds
        ---
        parameters:
            - name: name
              type: string
              paramType: query
              required: false
              description: Filters Rounds per Name via name
        """
        return super(RoundViewSet, self).list(request)

    def partial_update(self, request, pk=None):
        """
        Update an existing Round
        """
        return super(RoundViewSet, self).partial_update(request, pk=pk)

    def retrieve(self, request, pk=None):
        """
        Find an Round by ID
        """
        return super(RoundViewSet, self).retrieve(request, pk=pk)

    def update(self, request, pk=None):
        """
        Update an existing Round
        """
        return super(RoundViewSet, self).update(request, pk=pk)


class RunViewSet(CommonViewSet):
    """ Run resource. """

    queryset = models.Run.objects.all()
    serializer_class = serializers.RunSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        # 'name',
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


class ScenarioViewSet(CommonViewSet):
    """ Scenario resource. """

    queryset = models.Scenario.objects.all()
    serializer_class = serializers.ScenarioSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        # 'name',
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


class WebhookViewSet(CommonViewSet):
    """ Webhook resource. """

    queryset = models.Webhook.objects.all()
    serializer_class = serializers.WebhookSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        # 'name',
    )
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add a new Webhook
        """
        return super(WebhookViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        Delete an Webhook
        """
        return super(WebhookViewSet, self).destroy(request, pk=pk)

    def list(self, request):
        """
        Returns a list of Webhooks
        ---
        parameters:
            - name: name
              type: string
              paramType: query
              required: false
              description: Filters Webhooks per Name via name
        """
        return super(WebhookViewSet, self).list(request)

    def partial_update(self, request, pk=None):
        """
        Update an existing Webhook
        """
        return super(WebhookViewSet, self).partial_update(request, pk=pk)

    def retrieve(self, request, pk=None):
        """
        Find an Webhook by ID
        """
        return super(WebhookViewSet, self).retrieve(request, pk=pk)

    def update(self, request, pk=None):
        """
        Update an existing Webhook
        """
        return super(WebhookViewSet, self).update(request, pk=pk)


class WebhookLogViewSet(CommonViewSet):
    """ WebhookLog resource. """

    queryset = models.WebhookLog.objects.all()
    serializer_class = serializers.WebhookLogSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        # 'name',
    )
    ordering_fields = (
        'created',
        'modified',
    )

    def create(self, request):
        """
        Add a new WebhookLog
        """
        return super(WebhookLogViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        Delete an WebhookLog
        """
        return super(WebhookLogViewSet, self).destroy(request, pk=pk)

    def list(self, request):
        """
        Returns a list of Webhook Logs
        ---
        parameters:
            - name: name
              type: string
              paramType: query
              required: false
              description: Filters Webhook Logs per Name via name
        """
        return super(WebhookLogViewSet, self).list(request)

    def partial_update(self, request, pk=None):
        """
        Update an existing WebhookLog
        """
        return super(WebhookLogViewSet, self).partial_update(request, pk=pk)

    def retrieve(self, request, pk=None):
        """
        Find an WebhookLog by ID
        """
        return super(WebhookLogViewSet, self).retrieve(request, pk=pk)

    def update(self, request, pk=None):
        """
        Update an existing WebhookLog
        """
        return super(WebhookLogViewSet, self).update(request, pk=pk)


class WorldViewSet(CommonViewSet):
    """ World resource. """

    queryset = models.World.objects.all()
    serializer_class = serializers.WorldSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        # filters.SearchFilter,
    )
    filter_fields = (
        # 'name',
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
