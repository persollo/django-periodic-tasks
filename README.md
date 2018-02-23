
# django-periodic-tasks


Django app to process periodic and pending tasks
-----------------------------

1. **Please remember that this app is still in development.**

2. **Test this app before deploying it in production environments.**


```django-periodic-tasks``` (Periodic Tasks) is a reusable app for Django.


Crontab string syntax
---------------------

Full documentation for ```Crontab syntax``` can be found [here](http://pubs.opengroup.org/onlinepubs/9699919799/utilities/crontab.html) and [there](http://www.adminschoice.com/crontab-quick-reference).
Nice tool for generation: https://crontab.guru/

##### Crontab syntax in short:

A crontab string has five fields for specifying day, date and time followed by the command to be run at that interval.

```
*   *   *   *   *
-   -   -   -   -
|   |   |   |   |
|   |   |   |   +----- day of week (0 - 6) (Sunday=0)
|   |   |   +------- month (1 - 12)
|   |   +--------- day of month (1 - 31)
|   +----------- hour (0 - 23)
+------------- min (0 - 59)
```

##### Examples:

```
30 0 1 1,6,12 *   — 00:30 Hrs on 1st of Jan, June & Dec.
0 20 * 10 1-5     — 8.00 PM every weekday (Mon-Fri) only in Oct.
0 0 1,10,15 * *	  — midnight on 1st, 10th & 15th of month
5,10 0 10 * 1     — At 12.05,12.10 every Monday & on 10th of every month
```


How to use
----------

##### Install:

```bash
git+https://github.com/persollo/django-periodic-tasks.git

```

##### Add to Django INSTALLED_APPS:

```python
INSTALLED_APPS += ['periodic_tasks']
```

##### Create a directory for periodic tasks in one of your apps:

```
- app
|
+---- periodic_tasks
|       |
|       |---- __init__.py
|       |
|       |---- monday_emails.py
|
|---- ...
```

##### All periodic tasks functions MUST begin with "periodic_task":

```python
def periodic_task_send_monday_emails(user_id, email_title=None):
    return send_mail(user_id, email_title)
```

##### You MUST also initialize functions in __init__.py file:

```python
from .monday_emails import periodic_task_send_monday_emails
```

##### You can pass arguments tu functions just like you do it normally in Python code

```bash
123, 'Dream big! Work hard!'
```

##### To process tasks asynchronously, just add celery or kuyruk decorator:

```python
@kuyruk.task(queue='kuyruk')
def periodic_task_send_monday_emails(user_id, email_title=None):
    return send_mail(user_id, email_title)
```

License
-------

Periodic Tasks is licensed under the MIT license (see the ```LICENSE``` file for details).


Contribute
----------

If you have great ideas for Periodic Tasks, or if you like to improve something, feel free to fork this repository and/or create a pull request. I'm open for suggestions. If you like to discuss something with me, please open an issue.
