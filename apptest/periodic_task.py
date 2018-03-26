#coding:utf-8
#celery 定时任务

from celery import Celery
from celery.schedules import crontab

app = Celery()
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://localhost:6379/0'
CELERY_TIMEZONE = 'Asia/Shanghai'

from datetime import timedelta


#配置文件的形式
app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'myprojecttest.tasks.test',
        'schedule': 5.0,#5秒执行一次
        #'args': {16,16}
    },
}
app.conf.timezone = 'UTC'

'''
#函数形式
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    #add_periodic_task 会添加一条定时任务
    sender.add_periodic_task(10.0, test('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test('Happy Mondays!'),
    )


@app.task
def test(arg):
    print(arg)
'''


'''
celery -A apptest.periodic_task beat
celery -A apptest.periodic_task worker

'''


'''
#配置文件的形式
app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'myprojecttest.tasks.add',
        'schedule': 5.0,#30秒执行一次
        'args': (16, 16)
    },
}
app.conf.timezone = 'UTC'
from celery.schedules import crontab

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'tasks.add',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16),
    },
}#每周1的早上7.30执行tasks.add任务

'''

