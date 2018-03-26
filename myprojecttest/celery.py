# -*- coding: utf-8 -*-
'''
from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery_proj' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myprojecttest.settings')
app = Celery('myprojecttest',broker='redis://localhost:6379',backend='redis://localhost:6379', include=['myprojecttest.tasks'])

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#app.conf.broker_url = 'redis://localhost:6379'#Celery的默认broker是RabbitMQ, 仅需配置一行就可以
#app.conf.result_backend = 'redis://localhost:6379'
app.conf.update(
    result_expires=3600,
)

'''


'''
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
'''

from celery import Celery

app = Celery('myprojecttest',broker='redis://localhost:6379',backend='redis://localhost:6379', include=['myprojecttest.tasks'])

app.config_from_object('myprojecttest.config')

if __name__ == '__main__':
    app.start()
