from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from .. import chat
from .. import exceptions
from .. import models

"""
Serializers for models associated with a Run define a calculated `run_active` field.
If the model instance is not associated with a run (e.g. during a cascading delete), its value is None.
Otherwise, its value reflects the parent Run's active field.
"""


class DecisionSerializer(serializers.ModelSerializer):
    run_active = serializers.SerializerMethodField()
    role = serializers.PrimaryKeyRelatedField(
        queryset=models.Role.objects.all(),
        required=False,
        allow_null=True,
        default=None,
    )

    def get_run_active(self, obj):
        try:
            scenario = obj.period.scenario
            if scenario.world is not None:
                return scenario.world.run.active
            elif scenario.runuser is not None:
                return scenario.runuser.run.active
        except ObjectDoesNotExist:
            return None

    class Meta:
        model = models.Decision
        fields = "__all__"
        read_only_fields = ("created", "updated", "run_active")


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = "slug"
        model = models.Game
        fields = "__all__"
        read_only_fields = ("created", "updated")


class PeriodSerializer(serializers.ModelSerializer):
    run_active = serializers.SerializerMethodField()

    def get_run_active(self, obj):
        try:
            scenario = obj.scenario
            if scenario.world is not None:
                return scenario.world.run.active
            elif scenario.runuser is not None:
                return scenario.runuser.run.active
        except (ObjectDoesNotExist, AttributeError):
            return None

    class Meta:
        model = models.Period
        fields = "__all__"
        read_only_fields = ("created", "updated", "run_active")


class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Phase
        fields = "__all__"
        read_only_fields = ("created", "updated")


class ResultSerializer(serializers.ModelSerializer):
    run_active = serializers.SerializerMethodField()
    role = serializers.PrimaryKeyRelatedField(
        queryset=models.Role.objects.all(),
        required=False,
        allow_null=True,
        default=None,
    )

    def get_run_active(self, obj):
        try:
            scenario = obj.period.scenario
            if scenario.world is not None:
                return scenario.world.run.active
            elif scenario.runuser is not None:
                return scenario.runuser.run.active
        except (ObjectDoesNotExist, AttributeError):
            return None

    class Meta:
        model = models.Result
        fields = "__all__"
        read_only_fields = ("created", "updated", "run_active")


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = "__all__"
        read_only_fields = ("created", "updated")


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Run
        fields = "__all__"
        read_only_fields = ("created", "updated")


class RunUserSerializer(serializers.ModelSerializer):
    run_active = serializers.SerializerMethodField()

    def get_run_active(self, obj):
        try:
            return obj.run.active
        except (ObjectDoesNotExist, AttributeError):
            return None

    role = serializers.PrimaryKeyRelatedField(
        queryset=models.Role.objects.all(),
        required=False,
        allow_null=True,
        default=None,
    )
    email = serializers.CharField(source="user.email", required=False, read_only=True)
    first_name = serializers.CharField(
        source="user.first_name", required=False, read_only=True
    )
    last_name = serializers.CharField(
        source="user.last_name", required=False, read_only=True
    )
    role_name = serializers.CharField(
        source="role.name", required=False, read_only=True
    )

    class Meta:
        model = models.RunUser
        fields = "__all__"
        read_only_fields = ("created", "updated", "email", "run_active")


class ScenarioSerializer(serializers.ModelSerializer):
    run_active = serializers.SerializerMethodField()

    def get_run_active(self, obj):
        try:
            scenario = obj
            if scenario.world is not None:
                return scenario.world.run.active
            elif scenario.runuser is not None:
                return scenario.runuser.run.active
        except (ObjectDoesNotExist, AttributeError):
            return None

    class Meta:
        model = models.Scenario
        fields = "__all__"
        read_only_fields = ("created", "updated", "run_active")


class WorldSerializer(serializers.ModelSerializer):
    run_active = serializers.SerializerMethodField()

    def get_run_active(self, obj):
        try:
            return obj.run.active
        except (ObjectDoesNotExist, AttributeError):
            return None

    class Meta:
        model = models.World
        fields = "__all__"
        read_only_fields = ("created", "updated", "run_active")


class AuthSerializer(serializers.Serializer):
    authid = serializers.IntegerField(required=False, allow_null=True, default=None)
    email = serializers.EmailField(required=False, allow_null=True, default=None)
    password = serializers.CharField(max_length=200)

    def validate(self, data):
        if data["authid"] is None and data["email"] is None:
            raise serializers.ValidationError("'authid' or 'email' must be set")
        return data


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = "__all__"
        read_only_fields = ("created", "updated")


class RoomsForUserSerializer(serializers.Serializer):
    runuser = serializers.IntegerField(required=True)


class RoomsUserSerializer(serializers.Serializer):
    runuser = serializers.IntegerField(required=True)
    room = serializers.SlugField(required=True)


class RoomsCheckSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    room = serializers.SlugField(required=True)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = "__all__"
        read_only_fields = ("created", "updated")

    def validate_data(self, data):
        try:
            chat.validate_message(data)
        except exceptions.MessageValidationError as e:
            raise serializers.ValidationError(e)

        return data
