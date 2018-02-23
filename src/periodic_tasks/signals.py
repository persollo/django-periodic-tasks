from django.db.models.signals import post_save
from django.dispatch import receiver


from periodic_tasks.models import PeriodicTask


@receiver(post_save, sender=PeriodicTask)
def set_next_run_timestamp(sender, instance=None, created=False, **kwargs):
    """
    Signal to set next run after PeriodicTask instance creation
    """
    if created:
        instance.set_next_run_timestamp()
