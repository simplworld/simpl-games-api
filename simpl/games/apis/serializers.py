from rest_framework.serializers import ModelSerializer

from .. import models


class DecisionSerializer(ModelSerializer):
    class Meta:
        model = models.Decision
        read_only_fields = (
            'created',
            'updated',
        )


class GameSerializer(ModelSerializer):
    class Meta:
        lookup_field = 'slug'
        model = models.Game
        read_only_fields = (
            'created',
            'updated',
        )


class PeriodSerializer(ModelSerializer):
    class Meta:
        model = models.Period
        read_only_fields = (
            'created',
            'updated',
        )


class PhaseSerializer(ModelSerializer):
    class Meta:
        model = models.Phase
        read_only_fields = (
            'created',
            'updated',
        )


class ResultSerializer(ModelSerializer):
    class Meta:
        model = models.Result
        read_only_fields = (
            'created',
            'updated',
        )


class RoleSerializer(ModelSerializer):
    class Meta:
        model = models.Role
        read_only_fields = (
            'created',
            'updated',
        )


class RoundSerializer(ModelSerializer):
    class Meta:
        model = models.Round
        read_only_fields = (
            'created',
            'updated',
        )


class RunSerializer(ModelSerializer):
    class Meta:
        model = models.Run
        read_only_fields = (
            'created',
            'updated',
        )


class RunUserSerializer(ModelSerializer):
    class Meta:
        model = models.RunUser
        read_only_fields = (
            'created',
            'updated',
        )


class ScenarioSerializer(ModelSerializer):
    class Meta:
        model = models.Scenario
        read_only_fields = (
            'created',
            'updated',
        )


class WebhookSerializer(ModelSerializer):
    class Meta:
        model = models.Webhook
        read_only_fields = (
            'created',
            'updated',
        )


class WebhookLogSerializer(ModelSerializer):
    class Meta:
        model = models.WebhookLog
        read_only_fields = (
            'created',
            'updated',
        )


class WorldSerializer(ModelSerializer):
    class Meta:
        model = models.World
        read_only_fields = (
            'created',
            'updated',
        )
