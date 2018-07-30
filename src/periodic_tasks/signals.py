from django.db.models.signals import pre_save
from django.dispatch import receiver


from periodic_tasks.models import PeriodicTask


@receiver(pre_save, sender=PeriodicTask)
def set_next_run_timestamp(sender, instance=None, **kwargs):
    """
    Signal to set next run before PeriodicTask instance saving
    """
    instance.set_next_run_timestamp()
