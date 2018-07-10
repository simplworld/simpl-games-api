from rest_framework import serializers

from .. import models


class DecisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Decision
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
        )


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'slug'
        model = models.Game
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
        )


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Period
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
        )


class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Phase
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
        )


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Result
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
        )


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
        )


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Run
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
        )


class RunUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email', required=False,
                                  read_only=True)
    first_name = serializers.CharField(source='user.first_name',
                                       required=False, read_only=True)
    last_name = serializers.CharField(source='user.last_name', required=False,
                                      read_only=True)
    game_slug = serializers.CharField(source='game.slug', required=False,
                                      read_only=True)
    role_name = serializers.CharField(source='role.name', required=False,
                                      read_only=True)

    class Meta:
        model = models.RunUser
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
            'email',
            'game_slug',
        )


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Scenario
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
        )


class WorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.World
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
        )
