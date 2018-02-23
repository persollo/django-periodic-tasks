from distutils.core import setup

setup(
    name='django-periodic-tasks',
    version='0.0.1',
    packages=[
        'periodic_tasks',
        'periodic_tasks.migrations',
        'periodic_tasks.management',
        'periodic_tasks.management.commands',
    ],
    package_dir={'': 'src'},
    url='https://github.com/modgahead/django-periodic-tasks',
    license='MIT',
    author='Sergey Isayenko',
    description='Periodic tasks app for Django',
    install_requires=[
        'Django>=1.8',
    ],
    zip_safe=False
)
