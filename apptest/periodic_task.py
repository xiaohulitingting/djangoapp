#coding:utf-8
#celery 定时任务处理
from celery.schedules import crontab
from myprojecttest.celery import app
from datetime import timedelta
#配置文件的形式
app.conf.beat_schedule = {
    'add-every-59-seconds': {
        'task': 'apptest.tasks.add',#task： 指定任务的名字
        'schedule': timedelta(seconds=59),#秒执行一次(schedule : 设定任务的调度方式，可以是一个表示秒的整数，也可以是一个 timedelta 对象，或者是一个 crontab 对象（后面介绍），总之就是设定任务如何重复执行)
        'args': (16, 16)#args： 任务的参数列表kwargs：任务的参数字典options：所有 apply_async 所支持的参数
    },
    'add-every-50-seconds': {
        'task': 'apptest.tasks.lessnum',  # task： 指定任务的名字
        'schedule': timedelta(seconds=50),
        #
        # 秒执行一次(schedule : 设定任务的调度方式，可以是一个表示秒的整数，也可以是一个 timedelta 对象，或者是一个 crontab 对象（后面介绍），总之就是设定任务如何重复执行)
        'args': (20, 16)  # args： 任务的参数列表kwargs：任务的参数字典options：所有 apply_async 所支持的参数
    },
   'add-every-monday-morning': {
        'task': 'apptest.tasks.mul',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),#每周1的早上7.30执行tasks.add任务
        'args': (16, 16),
    },
}


'''
# 每分钟执行一次
c1 = crontab()

# 每天凌晨十二点执行
c2 = crontab(minute=0, hour=0)

# 每十五分钟执行一次
crontab(minute='*/15')

# 每周日的每一分钟执行一次
crontab(minute='*',hour='*', day_of_week='sun')

# 每周三，五的三点，七点和二十二点没十分钟执行一次
crontab(minute='*/10',hour='3,17,22', day_of_week='thu,fri')
'''

'''
#定时任务（如果程序含有定时任务 +异步处理任务）
celery -A apptest.periodic_task beat -l info
celery -A apptest.periodic_task worker -l info -P eventlet
celery -A myprojecttest flower --port=5555
#异步处理任务（如果没有定时任务）
celery -A myprojecttest worker -l info -P eventlet
'''


