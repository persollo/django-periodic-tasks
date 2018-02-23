from importlib import import_module

from django.apps import apps
from django.utils import timezone


def fetch_periodic_tasks():

    periodic_tasks = []
    periodic_tasks_modules = {}
    for app in apps.all_models.keys():
        try:
            periodic_tasks_modules[app] = import_module(app+'.periodic_tasks')
        except ModuleNotFoundError:
            pass
    for app, module in periodic_tasks_modules.items():
        namespace = dir(module)
        for attr in namespace:
            if callable(getattr(module, attr)) and attr.startswith('periodic_task_'):
                periodic_tasks.append('%s.%s' % (module.__name__, attr))
    return periodic_tasks


def parse_args(task):
    if not task.arguments:
        return [], {}
    all_arguments = [item.strip(' ') for item in task.arguments.split(',')]
    args = []
    kwargs = {}
    for argument in all_arguments:
        if '=' not in argument:
            args.append(argument)
        else:
            [key, value] = argument.split('=')
            kwargs.update({key: value})
    return args, kwargs


def execute_tasks():
    from periodic_tasks.models import PeriodicTask
    all_tasks = PeriodicTask.objects.filter(
        is_active=True,
        next_run_timestamp__isnull=False,
    )
    for task in all_tasks:
        ts_now = int(timezone.localtime().timestamp())
        if task.next_run_timestamp and ts_now >= task.next_run_timestamp:
            module_name = '.'.join(task.task.split('.')[:-1])
            method_name = task.task.split('.')[-1]
            task_module = import_module(module_name)
            task_method = getattr(task_module, method_name)
            (args, kwargs) = parse_args(task)
            task_method(*args, **kwargs)
            task.set_next_run_timestamp(update=True)
            print(task.task + ' EXECUTED at ' + str(timezone.localtime()))
