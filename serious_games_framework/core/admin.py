from django.contrib import admin


class TimeStampedAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class TimeStampedTabularInline(admin.TabularInline):
    exclude = ('created', 'updated')
