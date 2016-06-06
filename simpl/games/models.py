from django.conf import settings
from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from thorn import model_reverser, webhook_model

from . import events

from simpl.core import managers
from simpl.core.mixins import AbstractTimeStampedModel


@python_2_unicode_compatible
@webhook_model(
    on_create=events.on_decision_created,
    reverse=model_reverser('simpl_api:decision-detail', pk='pk'),
    sender_field='game.user'
)
class Decision(AbstractTimeStampedModel):
    """Decision model"""

    name = models.CharField(max_length=100)
    data = JSONField(blank=True, null=True)
    period = models.ForeignKey(
        'Period',
        related_name='decisions'
    )
    role = models.ForeignKey(
        'Role',
        blank=True,
        null=True,
        related_name='decisions'
    )

    class Meta(object):
        verbose_name = _('decision')
        verbose_name_plural = _('decisions')

    def __str__(self):
        return self.name

    @property
    def game(self):
        return self.period.game

    def webhook_payload(self):
        from .apis.serializers import DecisionSerializer

        return DecisionSerializer(self).data


@python_2_unicode_compatible
@webhook_model(
    on_create=events.on_game_created,
    reverse=model_reverser('simpl_api:game-detail', slug='slug'),
    sender_field='user'
)
class Game(AbstractTimeStampedModel):
    """Game model"""

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, blank=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name='games'
    )

    objects = managers.ActiveQuerySet.as_manager()

    class Meta(object):
        verbose_name = _('game')
        verbose_name_plural = _('games')

    def save(self, *args, **kwargs):
        """
        Overrides a Game's default save method to populate the slug
        field if `Game.name` is blank.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def webhook_payload(self):
        from .apis.serializers import GameSerializer

        return GameSerializer(self).data


@python_2_unicode_compatible
@webhook_model(
    on_create=events.on_period_created,
    reverse=model_reverser('simpl_api:period-detail', pk='pk'),
    sender_field='game.user'
)
class Period(AbstractTimeStampedModel):
    """Period model"""

    scenario = models.ForeignKey(
        'Scenario',
        related_name='periods'
    )
    order = models.IntegerField(default=0)
    data = JSONField(blank=True, null=True)

    class Meta(object):
        verbose_name = _('period')
        verbose_name_plural = _('periods')

    def __str__(self):
        return '{0}: {1}'.format(
            self.scenario.name,
            self.order
        )

    @property
    def game(self):
        return self.scenario.game

    def webhook_payload(self):
        from .apis.serializers import PeriodSerializer

        return PeriodSerializer(self).data


@python_2_unicode_compatible
@webhook_model(
    on_create=events.on_phase_created,
    reverse=model_reverser('simpl_api:phase-detail', pk='pk'),
    sender_field='game.user'
)
class Phase(AbstractTimeStampedModel):
    """Phase model"""

    name = models.CharField(max_length=100)
    game = models.ForeignKey(
        'Game',
        related_name='phases'
    )
    order = models.IntegerField(blank=True, null=True)

    class Meta(object):
        verbose_name = _('phase')
        verbose_name_plural = _('phases')

    def __str__(self):
        return self.name

    def webhook_payload(self):
        from .apis.serializers import PhaseSerializer

        return PhaseSerializer(self).data


@python_2_unicode_compatible
@webhook_model(
    on_create=events.on_result_created,
    reverse=model_reverser('simpl_api:result-detail', pk='pk'),
    # sender_field='game.user'
)
class Result(AbstractTimeStampedModel):
    """Result model"""

    name = models.CharField(max_length=100)
    data = JSONField(blank=True, null=True)
    period = models.ForeignKey(
        'Period',
        related_name='results'
    )
    role = models.ForeignKey(
        'Role',
        blank=True,
        null=True,
        related_name='results'
    )

    class Meta(object):
        verbose_name = _('result')
        verbose_name_plural = _('results')

    def __str__(self):
        return self.name

    def webhook_payload(self):
        from .apis.serializers import ResultSerializer

        return ResultSerializer(self).data


@python_2_unicode_compatible
class Role(AbstractTimeStampedModel):
    """Role model"""

    name = models.CharField(max_length=100)
    game = models.ForeignKey(
        'Game',
        related_name='roles',
        blank=True,
        null=True,
    )
    data = JSONField(blank=True, null=True)

    class Meta(object):
        verbose_name = _('role')
        verbose_name_plural = _('roles')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
@webhook_model(
    on_create=events.on_round_created,
    reverse=model_reverser('simpl_api:round-detail', pk='pk'),
    sender_field='game.user'
)
class Round(AbstractTimeStampedModel):
    """Round model"""

    name = models.CharField(max_length=100)
    world = models.ForeignKey(
        'World',
        related_name='rounds'
    )
    order = models.IntegerField(blank=True, null=True)
    data = JSONField(blank=True, null=True)

    class Meta(object):
        verbose_name = _('round')
        verbose_name_plural = _('rounds')

    def __str__(self):
        return self.name

    @property
    def game(self):
        return self.world.game

    def webhook_payload(self):
        from .apis.serializers import RoundSerializer

        return RoundSerializer(self).data


@python_2_unicode_compatible
@webhook_model(
    on_create=events.on_run_created,
    reverse=model_reverser('simpl_api:run-detail', pk='pk'),
    sender_field='game.user'
)
class Run(AbstractTimeStampedModel):
    """Run model"""

    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    game = models.ForeignKey(
        'Game',
        related_name='runs'
    )
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    data = JSONField(blank=True, null=True)

    objects = managers.ActiveQuerySet.as_manager()

    class Meta(object):
        verbose_name = _('run')
        verbose_name_plural = _('runs')

    def __str__(self):
        return self.name

    def webhook_payload(self):
        from .apis.serializers import RunSerializer

        return RunSerializer(self).data


@python_2_unicode_compatible
@webhook_model(
    on_create=events.on_runuser_created,
    reverse=model_reverser('simpl_api:runuser-detail', pk='pk'),
    sender_field='user'
)
class RunUser(AbstractTimeStampedModel):
    """Run User model"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='run_users'
    )
    run = models.ForeignKey(
        'Run',
        related_name='run_users'
    )
    world = models.ForeignKey(
        'World',
        blank=True,
        null=True,
        related_name='run_users'
    )
    role = models.ForeignKey(
        'Role',
        blank=True,
        null=True,
        related_name='run_users'
    )
    facilitator = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    data = JSONField(blank=True, null=True)

    objects = managers.ActiveQuerySet.as_manager()

    class Meta(object):
        verbose_name = _('run user')
        verbose_name_plural = _('run users')

    def __str__(self):
        return self.user.__str__()

    def webhook_payload(self):
        from .apis.serializers import RunUserSerializer

        return RunUserSerializer(self).data


@python_2_unicode_compatible
@webhook_model(
    on_create=events.on_scenario_created,
    reverse=model_reverser('simpl_api:scenario-detail', pk='pk'),
    sender_field='game.user'
)
class Scenario(AbstractTimeStampedModel):
    """Scenario model"""

    name = models.CharField(max_length=100)
    creator_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name='scenarios'
    )
    round = models.ForeignKey(
        'Round',
        related_name='scenarios'
    )
    player_periods = models.IntegerField(blank=True, null=True)
    current_period = models.ForeignKey(
        'Period',
        blank=True,
        null=True,
        related_name='current_period_scenarios'
    )
    last_period = models.ForeignKey(
        'Period',
        blank=True,
        null=True,
        related_name='last_period_scenarios'
    )
    seed_periods = models.IntegerField(blank=True, null=True)
    total_periods = models.IntegerField(blank=True, null=True)

    class Meta(object):
        verbose_name = _('scenario')
        verbose_name_plural = _('scenarios')

    def __str__(self):
        return self.name

    @property
    def game(self):
        return self.round.game

    def webhook_payload(self):
        from .apis.serializers import ScenarioSerializer

        return ScenarioSerializer(self).data


@python_2_unicode_compatible
@webhook_model(
    on_create=events.on_world_created,
    reverse=model_reverser('simpl_api:world-detail', pk='pk'),
    sender_field='game.user'
)
class World(AbstractTimeStampedModel):
    """World model"""

    name = models.CharField(max_length=100)
    run = models.ForeignKey(
        'Run',
        related_name='worlds'
    )
    data = JSONField(blank=True, null=True)
    canvas_ids = ArrayField(
        ArrayField(
            models.IntegerField()
        ),
        blank=True,
        null=True
    )

    class Meta(object):
        verbose_name = _('world')
        verbose_name_plural = _('worlds')

    def __str__(self):
        return self.name

    @property
    def game(self):
        return self.run.game

    def webhook_payload(self):
        from .apis.serializers import WorldSerializer

        return WorldSerializer(self).data
