from rest_framework import serializers

from .models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = [
            'id',
            'event',
            'url',
            'user',
            'connected',
            'erroring',
            'last_error',
            'last_error_status',
            'last_error_content',
            'created',
            'modified',
        ]
        read_only_fields = [
            'id',
            'created',
            'modified',
            'user',
            'connected',
            'erroring',
            'last_error',
            'last_error_status',
            'last_error_content',
        ]
