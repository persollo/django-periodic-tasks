from croniter import croniter

from django.utils import timezone
from django.db import models

from periodic_tasks.utils import fetch_periodic_tasks
from periodic_tasks.validators import validate_crontab_string


def tasks_as_choices():
    for task in fetch_periodic_tasks():
        yield (task, task)


class PeriodicTask(models.Model):

    task = models.CharField(
        max_length=256,
        choices=tasks_as_choices(),
    )
    arguments = models.CharField(
        max_length=256,
        blank=True,
        default='',
    )
    crontab_string = models.CharField(
        max_length=256,
        validators=[validate_crontab_string],
        blank=True,
        default='* * * * *',
    )
    last_run_dt = models.DateTimeField(blank=True, null=True)
    next_run_timestamp = models.IntegerField(blank=True, null=True)
    is_one_time_run = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-last_run_dt',)

    def __str__(self):
        return self.task

    @property
    def next_run_dt(self):
        if self.next_run_timestamp:
            return timezone.datetime.fromtimestamp(self.next_run_timestamp)
        return None

    def set_next_run_timestamp(self, update=False):
        if update:
            self.last_run_dt = timezone.localtime()
        if self.is_one_time_run and update:
            self.next_run_timestamp = None
            self.is_active = False
        else:
            self.next_run_timestamp = croniter(
                self.crontab_string,
                timezone.localtime()
            ).get_next()
        return self.save()
