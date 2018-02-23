from django.apps import AppConfig


class PeriodicTasksConfig(AppConfig):
    name = 'periodic_tasks'
    verbose_name = "Periodic Tasks"

    def ready(self):
        from periodic_tasks import signals  # noqa: F401 imported but unused
