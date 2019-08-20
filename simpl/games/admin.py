from django.contrib import admin

from . import models
from simpl.core.admin import TimeStampedAdmin

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
        'role',
    ]


@admin.register(models.Game)
class GameAdmin(TimeStampedAdmin):
    list_display = (
        'name',
        'slug',
        'active',
    )
    prepopulated_fields = {'slug': ('name',)}


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
        'role',
    ]


@admin.register(models.Role)
class RoleAdmin(TimeStampedAdmin):
    list_display = (
        'name',
        'game',
    )
    raw_id_fields = [
        'game',
    ]


@admin.register(models.Run)
class RunAdmin(TimeStampedAdmin):
    list_display = (
        'name',
        'active',
        'game',
    )
    raw_id_fields = [
        'game',
    ]


@admin.register(models.RunUser)
class RunUserAdmin(TimeStampedAdmin):
    list_display = (
        'user',
        'run',
        'world',
        'active',
        'leader',
    )
    raw_id_fields = [
        'user',
        'run',
        'world',
        'role',
    ]


@admin.register(models.Scenario)
class ScenarioAdmin(TimeStampedAdmin):
    list_display = (
        'name',
        'runuser',
        'world',
    )
    raw_id_fields = [
        'runuser',
        'world',
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
