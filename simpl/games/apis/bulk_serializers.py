from rest_framework import serializers

from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
)

from .. import models


class BulkDecisionSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Decision
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
        )
        list_serializer_class = BulkListSerializer  # to handle update


class BulkPeriodSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Period
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
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
    class Meta:
        model = models.Result
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
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

        list_serializer_class = BulkListSerializer  # to handle update


class BulkScenarioSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Scenario
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
        )
        list_serializer_class = BulkListSerializer  # to handle update


class BulkWorldSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.World
        fields = '__all__'
        read_only_fields = (
            'created',
            'updated',
        )
        list_serializer_class = BulkListSerializer  # to handle update
