from django.contrib import admin

from . import models
from serious_games_framework.admin import TimeStampedAdmin, TimeStampedTabularInline


# Inlines

class WebhookInline(TimeStampedTabularInline):
    model = models.Webhook
    list_display = (
        'name',
        'game',
    )
    raw_id_fields = [
        'game',
    ]


# Model Admins

@admin.register(models.Decision)
class DecisionAdmin(TimeStampedAdmin):
    list_display = (
        'name',
        'period',
        'created',
    )
    raw_id_fields = [
        'period',
    ]


@admin.register(models.Game)
class GameAdmin(TimeStampedAdmin):
    inlines = [
        WebhookInline,
    ]
    list_display = (
        'name',
        'active',
    )


@admin.register(models.Period)
class PeriodAdmin(TimeStampedAdmin):
    list_display = (
        'scenario',
        'order',
        'created',
    )
    raw_id_fields = [
        'scenario',
    ]


@admin.register(models.Phase)
class PhaseAdmin(TimeStampedAdmin):
    list_display = (
        'name',
        'game',
        'order',
    )
    raw_id_fields = [
        'game',
    ]


@admin.register(models.Result)
class ResultAdmin(TimeStampedAdmin):
    list_display = (
        'name',
        'period',
        'created',
    )
    raw_id_fields = [
        'period',
    ]


@admin.register(models.Role)
class RoleAdmin(TimeStampedAdmin):
    list_display = (
        'name',
        'world',
    )
    raw_id_fields = [
        'world',
    ]


@admin.register(models.Round)
class RoundAdmin(TimeStampedAdmin):
    list_display = (
        'name',
        'world',
        'order',
    )
    raw_id_fields = [
        'world',
    ]


@admin.register(models.Run)
class RunAdmin(TimeStampedAdmin):
    list_display = (
        'name',
        'active',
        'game',
        'start_date',
        'end_date',
    )
    raw_id_fields = [
        'game',
    ]


@admin.register(models.Scenario)
class ScenarioAdmin(TimeStampedAdmin):
    list_display = (
        'name',
        'creator_user',
        'round',
    )
    raw_id_fields = [
        'creator_user',
        'round',
        'current_period',
        'last_period',
    ]


@admin.register(models.Webhook)
class WebhookAdmin(TimeStampedAdmin):
    list_display = (
        'name',
        'game',
    )
    raw_id_fields = [
        'game',
    ]


@admin.register(models.WebhookLog)
class WebhookLogAdmin(TimeStampedAdmin):
    list_display = (
        'webhook',
        'status',
        'last_delivery',
        'created',
    )
    raw_id_fields = [
        'webhook',
    ]


@admin.register(models.World)
class WorldAdmin(TimeStampedAdmin):
    list_display = (
        'name',
        'run',
    )
    raw_id_fields = [
        'run',
    ]
