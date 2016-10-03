from rest_framework import serializers

from .. import models


class DecisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Decision
        read_only_fields = (
            'created',
            'updated',
        )


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'slug'
        model = models.Game
        read_only_fields = (
            'created',
            'updated',
        )


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Period
        read_only_fields = (
            'created',
            'updated',
        )


class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Phase
        read_only_fields = (
            'created',
            'updated',
        )


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Result
        read_only_fields = (
            'created',
            'updated',
        )


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        read_only_fields = (
            'created',
            'updated',
        )


class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Round
        read_only_fields = (
            'created',
            'updated',
        )


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Run
        read_only_fields = (
            'created',
            'updated',
        )


class RunUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', required=False, read_only=True)
    first_name = serializers.CharField(source='user.first_name', required=False, read_only=True)
    last_name = serializers.CharField(source='user.last_name', required=False, read_only=True)
    email = serializers.CharField(source='user.email', required=False, read_only=True)
    game_slug = serializers.CharField(source='game.slug', required=False, read_only=True)
    role_name = serializers.CharField(source='role.name', required=False, read_only=True)

    class Meta:
        model = models.RunUser
        read_only_fields = (
            'created',
            'updated',
            'username',
            'game_slug',
        )


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Scenario
        read_only_fields = (
            'created',
            'updated',
        )


class WorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.World
        read_only_fields = (
            'created',
            'updated',
        )
