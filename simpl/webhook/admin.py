from django.contrib import admin

from . import models


@admin.register(models.Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        'url',
        'event',
        'user',
        'connected',
        'erroring',
        'last_error',
        'created',
    )
