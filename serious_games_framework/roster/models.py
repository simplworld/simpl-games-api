from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from serious_games_framework.mixins import AbstractTimeStampedModel


@python_2_unicode_compatible
class Action(AbstractTimeStampedModel):
    scenario = models.ForeignKey(
        'Scenario',
        related_name='actions'
    )
    position = models.IntegerField(blank=True, null=True)
    data = JSONField(blank=True, null=True)

    class Meta(object):
        verbose_name = _('action')
        verbose_name_plural = _('actions')

    def __str__(self):
        return '{0}: {1}'.format(
            self.scenario.name,
            self.position
        )


class Decision(AbstractTimeStampedModel):
    data = JSONField(blank=True, null=True)
    action = models.ForeignKey(
        'Action',
        related_name='decisions'
    )

    class Meta(object):
        verbose_name = _('decision')
        verbose_name_plural = _('decisions')


@python_2_unicode_compatible
class Game(AbstractTimeStampedModel):
    name = models.CharField(max_length=100)
    admins = models.ManyToManyField(
        'users.User',
        blank=True,
        related_name='game_admins'
    )
    superusers = models.ManyToManyField(
        'users.User',
        blank=True,
        related_name='game_superusers'
    )
    user = models.ForeignKey(
        'users.User',
        related_name='games'
    )

    class Meta(object):
        verbose_name = _('game')
        verbose_name_plural = _('games')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Phase(AbstractTimeStampedModel):
    name = models.CharField(max_length=100)
    game = models.ForeignKey(
        'Game',
        related_name='phases'
    )
    rounds_count = models.IntegerField(default=0)
    position = models.IntegerField(blank=True, null=True)

    class Meta(object):
        verbose_name = _('phase')
        verbose_name_plural = _('phases')

    def __str__(self):
        return self.name


class Result(AbstractTimeStampedModel):
    data = JSONField(blank=True, null=True)
    action = models.ForeignKey(
        'Action',
        related_name='results'
    )

    class Meta(object):
        verbose_name = _('result')
        verbose_name_plural = _('results')


@python_2_unicode_compatible
class Role(AbstractTimeStampedModel):
    name = models.CharField(max_length=100)
    world = models.ForeignKey(
        'World',
        related_name='roles'
    )

    class Meta(object):
        verbose_name = _('role')
        verbose_name_plural = _('roles')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Round(AbstractTimeStampedModel):
    name = models.CharField(max_length=100)
    world = models.ForeignKey(
        'World',
        related_name='rounds'
    )
    phase = models.ForeignKey(
        'Phase',
        related_name='rounds'
    )
    position = models.IntegerField(blank=True, null=True)
    state = JSONField(blank=True, null=True)

    class Meta(object):
        verbose_name = _('round')
        verbose_name_plural = _('rounds')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Run(AbstractTimeStampedModel):
    name = models.CharField(max_length=100)
    game = models.ForeignKey(
        'Game',
        related_name='runs'
    )
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta(object):
        verbose_name = _('run')
        verbose_name_plural = _('runs')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Scenario(AbstractTimeStampedModel):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        'users.User',
        related_name='scenarios'
    )
    round = models.ForeignKey(
        'Round',
        related_name='scenarios'
    )

    class Meta(object):
        verbose_name = _('scenario')
        verbose_name_plural = _('scenarios')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Webhook(AbstractTimeStampedModel):
    name = models.CharField(max_length=100)
    game = models.ForeignKey(
        'Game',
        related_name='webhooks'
    )
    url = models.URLField(max_length=1000)

    class Meta(object):
        verbose_name = _('webhook')
        verbose_name_plural = _('webhooks')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class WebhookLog(AbstractTimeStampedModel):
    webhook = models.ForeignKey(
        'Webhook',
        related_name='webhooklogs'
    )
    status = models.IntegerField(blank=True, null=True)
    last_delivery = models.DateTimeField(blank=True, null=True)

    class Meta(object):
        verbose_name = _('webhook log')
        verbose_name_plural = _('webhook logs')

    def __str__(self):
        return '{0}: {1}'.format(
            self.status,
            self.webhook.name,
        )


@python_2_unicode_compatible
class World(AbstractTimeStampedModel):
    name = models.CharField(max_length=100)
    phase = models.ForeignKey(
        'Phase',
        related_name='worlds'
    )
    run = models.ForeignKey(
        'Run',
        related_name='worlds'
    )
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
