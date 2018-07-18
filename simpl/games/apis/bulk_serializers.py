from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers

from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
)

from .. import models

"""
Serializers for models associated with a Run define a calculated `run_active` field.
If the model instance is not associated with a run (e.g. during a cascading delete), its value is None. 
Otherwise, its value reflects the parent Run's active field. 
"""


class BulkDecisionSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    run_active = serializers.SerializerMethodField()

    def get_run_active(self, obj):
        try:
            scenario = obj.period.scenario
            if scenario.world is not None:
                return scenario.world.run.active
            elif scenario.runuser is not None:
                return scenario.runuser.run.active
        except Exception as e:
            return None

    class Meta:
        model = models.Decision
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
            'run_active',
        )
        list_serializer_class = BulkListSerializer  # to handle update


class BulkPeriodSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    run_active = serializers.SerializerMethodField()

    def get_run_active(self, obj):
        try:
            scenario = obj.scenario
            if scenario.world is not None:
                return scenario.world.run.active
            elif scenario.runuser is not None:
                return scenario.runuser.run.active
        except Exception as e:
            return None

    class Meta:
        model = models.Period
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
            'run_active',
        )
        list_serializer_class = BulkListSerializer  # to handle update


class BulkPhaseSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Phase
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
        )
        list_serializer_class = BulkListSerializer  # to handle update


class BulkResultSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    run_active = serializers.SerializerMethodField()

    def get_run_active(self, obj):
        try:
            scenario = obj.period.scenario
            if scenario.world is not None:
                return scenario.world.run.active
            elif scenario.runuser is not None:
                return scenario.runuser.run.active
        except Exception as e:
            return None

    class Meta:
        model = models.Result
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
            'run_active',
        )
        list_serializer_class = BulkListSerializer  # to handle update


class BulkRoleSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
        )
        list_serializer_class = BulkListSerializer  # to handle update


class BulkRunSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Run
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
        )
        list_serializer_class = BulkListSerializer  # to handle update


class BulkRunUserSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    run_active = serializers.SerializerMethodField()

    def get_run_active(self, obj):
        try:
            return obj.run.active
        except Exception as e:
            return None

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
            'run_active',
        )

        list_serializer_class = BulkListSerializer  # to handle update


class BulkScenarioSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    run_active = serializers.SerializerMethodField()

    def get_run_active(self, obj):
        try:
            scenario = obj
            if scenario.world is not None:
                return scenario.world.run.active
            elif scenario.runuser is not None:
                return scenario.runuser.run.active
        except Exception as e:
            return None

    class Meta:
        model = models.Scenario
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
            'run_active',
        )
        list_serializer_class = BulkListSerializer  # to handle update


class BulkWorldSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    run_active = serializers.SerializerMethodField()

    def get_run_active(self, obj):
        try:
            return obj.run.active
        except Exception as e:
            return None

    class Meta:
        model = models.World
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
            'run_active',
        )
        list_serializer_class = BulkListSerializer  # to handle update
