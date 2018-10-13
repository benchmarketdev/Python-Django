from __future__ import absolute_import, unicode_literals
import os

from django.conf import settings

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial.settings')

app = Celery('hotenv', backend='amqp', broker='amqp://guest:guest@localhost:5672//')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, related_name='tasks')

app.conf.update(
    # CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
)
