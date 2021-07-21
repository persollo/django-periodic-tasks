import time
import traceback

from django.core.management.base import BaseCommand

from periodic_tasks.utils import execute_tasks


class Command(BaseCommand):
    help = 'Run periodic tasks loop'

    def handle(self, *args, **options):
        """
        Loop runs every 10 seconds
        """
        while True:
            try:
                execute_tasks()
                # TODO: Use success callback function here
            except Exception as e:
                # TODO: Use error callback function here
                print(e)
                traceback.print_exc()
                pass
            time.sleep(10)
