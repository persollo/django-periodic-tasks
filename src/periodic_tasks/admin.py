from django.contrib import admin

from periodic_tasks import models


@admin.register(models.PeriodicTask)
class PrediodicTaskAdmin(admin.ModelAdmin):
    exclude = (
        'last_run_dt',
        'next_run_timestamp',
    )
    list_filter = (
        'is_active',
        'is_one_time_run',
    )
    list_display = (
        'task',
        'arguments',
        'last_run_dt',
        'next_run_dt',
        'is_active',
        'is_one_time_run',
    )
    list_editable = (
        'is_active',
    )
