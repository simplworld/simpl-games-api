from django.conf import settings
from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from simpl.core import managers
from simpl.core.decorators import cached_method
from simpl.core.mixins import AbstractTimeStampedModel

from . import events


class Decision(AbstractTimeStampedModel):
    """Decision model"""

    name = models.CharField(max_length=100)
    data = JSONField(default=dict, blank=True)
    period = models.ForeignKey(
        'Period',
        related_name='decisions',
        on_delete=models.CASCADE,
    )
    role = models.ForeignKey(
        'Role',
        blank=True,
        null=True,
        related_name='decisions',
        on_delete=models.CASCADE,
    )

    class Meta(object):
        unique_together = ('name', 'period', 'role')
        verbose_name = _('decision')
        verbose_name_plural = _('decisions')
        ordering = ('pk',)

    def __str__(self):
        return self.name

    @property
    @cached_method("decisions:{.pk}:game")
    def game(self):
        return self.period.game

    def webhook_payload(self):
        from .apis.serializers import DecisionSerializer

        return DecisionSerializer(self).data


class Game(AbstractTimeStampedModel):
    """Game model"""

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=250, blank=True, unique=True)
    active = models.BooleanField(default=True)
    data = JSONField(default=dict, blank=True)

    objects = managers.ActiveQuerySet.as_manager()

    class Meta(object):
        verbose_name = _('game')
        verbose_name_plural = _('games')
        ordering = ('pk',)

    def save(self, **kwargs):
        """
        Overrides a Game's default save method to populate the slug
        field if `Game.name` is blank.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(**kwargs)

    def __str__(self):
        return self.name

    def webhook_payload(self):
        from .apis.serializers import GameSerializer

        return GameSerializer(self).data


class Period(AbstractTimeStampedModel):
    """Period model"""

    scenario = models.ForeignKey(
        'Scenario',
        related_name='periods',
        on_delete=models.CASCADE,
    )
    order = models.IntegerField(default=0, db_index=True)
    data = JSONField(default=dict, blank=True)

    class Meta(object):
        unique_together = ('scenario', 'order')
        verbose_name = _('period')
        verbose_name_plural = _('periods')
        ordering = ('pk',)

    def __str__(self):
        return '{0}: {1}'.format(
            self.scenario.name,
            self.order
        )

    @property
    @cached_method("periods:{.pk}:game")
    def game(self):
        return self.scenario.game

    def webhook_payload(self):
        from .apis.serializers import PeriodSerializer

        return PeriodSerializer(self).data


class Phase(AbstractTimeStampedModel):
    """Phase model"""

    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    game = models.ForeignKey(
        'Game',
        related_name='phases',
        on_delete=models.CASCADE,
    )
    order = models.PositiveSmallIntegerField(blank=True, null=True,
                                             db_index=True)

    class Meta(object):
        unique_together = ('name', 'game')
        verbose_name = _('phase')
        verbose_name_plural = _('phases')
        ordering = ('pk',)

    def __str__(self):
        return self.name

    def webhook_payload(self):
        from .apis.serializers import PhaseSerializer

        return PhaseSerializer(self).data


class Result(AbstractTimeStampedModel):
    """Result model"""

    name = models.CharField(max_length=100)
    data = JSONField(default=dict, blank=True)
    period = models.ForeignKey(
        'Period',
        related_name='results',
        on_delete=models.CASCADE,
    )
    role = models.ForeignKey(
        'Role',
        blank=True,
        null=True,
        related_name='results',
        on_delete=models.CASCADE,
    )

    class Meta(object):
        unique_together = ('name', 'period', 'role')
        verbose_name = _('result')
        verbose_name_plural = _('results')
        ordering = ('pk',)

    def __str__(self):
        return self.name

    @property
    @cached_method("results:{.pk}:game")
    def game(self):
        return self.period.game

    def webhook_payload(self):
        from .apis.serializers import ResultSerializer

        return ResultSerializer(self).data


class Role(AbstractTimeStampedModel):
    """Role model"""

    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    game = models.ForeignKey(
        'Game',
        related_name='roles',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    data = JSONField(default=dict, blank=True)

    class Meta(object):
        unique_together = ('name', 'game')
        verbose_name = _('role')
        verbose_name_plural = _('roles')
        ordering = ('created',)

    def __str__(self):
        return self.name

    def webhook_payload(self):
        from .apis.serializers import RoleSerializer

        return RoleSerializer(self).data


class Run(AbstractTimeStampedModel):
    """Run model"""

    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    game = models.ForeignKey(
        'Game',
        related_name='runs',
        on_delete=models.CASCADE,
    )
    data = JSONField(default=dict, blank=True)
    phase = models.ForeignKey(
        'Phase',
        blank=True,
        null=True,
        related_name='+',
        on_delete=models.CASCADE,
    )

    objects = managers.ActiveQuerySet.as_manager()

    class Meta(object):
        verbose_name = _('run')
        verbose_name_plural = _('runs')
        ordering = ('pk',)

    def __str__(self):
        return self.name

    def webhook_payload(self):
        from .apis.serializers import RunSerializer

        return RunSerializer(self).data


class RunUser(AbstractTimeStampedModel):
    """Run User model"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='run_users',
        on_delete=models.CASCADE,
    )
    run = models.ForeignKey(
        'Run',
        related_name='run_users',
        on_delete=models.CASCADE,
    )
    world = models.ForeignKey(
        'World',
        blank=True,
        null=True,
        related_name='run_users',
        on_delete=models.CASCADE,
    )
    role = models.ForeignKey(
        'Role',
        blank=True,
        null=True,
        related_name='run_users',
        on_delete=models.CASCADE,
    )
    leader = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    data = JSONField(default=dict, blank=True)

    objects = managers.ActiveQuerySet.as_manager()

    class Meta(object):
        unique_together = ('user', 'run')
        verbose_name = _('run user')
        verbose_name_plural = _('run users')
        ordering = ('pk',)

    def __str__(self):
        return self.user.__str__()

    @property
    @cached_method("runusers:{.pk}:game")
    def game(self):
        return self.run.game

    def webhook_payload(self):
        from .apis.serializers import RunUserSerializer

        return RunUserSerializer(self).data


class Scenario(AbstractTimeStampedModel):
    """Scenario model"""

    name = models.CharField(max_length=100, db_index=True)

    runuser = models.ForeignKey(
        'RunUser',
        blank=True,
        null=True,
        related_name='scenarios',
        on_delete=models.CASCADE,
    )
    world = models.ForeignKey(
        'World',
        blank=True,
        null=True,
        related_name='scenarios',
        on_delete=models.CASCADE,
    )

    data = JSONField(default=dict, blank=True)

    class Meta(object):
        verbose_name = _('scenario')
        verbose_name_plural = _('scenarios')
        ordering = ('pk',)

    def __str__(self):
        return self.name

    @property
    @cached_method("scenarios:{.pk}:game")
    def game(self):
        if self.world:
            return self.world.game
        else:
            return self.runuser.game

    def webhook_payload(self):
        from .apis.serializers import ScenarioSerializer

        return ScenarioSerializer(self).data


class World(AbstractTimeStampedModel):
    """World model"""

    name = models.CharField(max_length=100)
    run = models.ForeignKey(
        'Run',
        related_name='worlds',
        on_delete=models.CASCADE,
    )
    data = JSONField(default=dict, blank=True)
    external_ids = ArrayField(
        ArrayField(
            models.IntegerField()
        ),
        blank=True,
        null=True
    )

    class Meta(object):
        unique_together = ('name', 'run')
        verbose_name = _('world')
        verbose_name_plural = _('worlds')
        ordering = ('pk',)

    def __str__(self):
        return self.name

    @property
    @cached_method("worlds:{.pk}:game")
    def game(self):
        return self.run.game

    def webhook_payload(self):
        from .apis.serializers import WorldSerializer

        return WorldSerializer(self).data
