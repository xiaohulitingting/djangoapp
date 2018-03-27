#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Create your tasks here
#from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time
from myprojecttest.celery import app


@shared_task
def add(x, y):
    print("--add--")
    a=x+y
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def lessnum(x, y):
    return x - y
@shared_task
def xsum(numbers):
    return sum(numbers)

#@app.task(在django中可以这样写)
@shared_task
def sleepseconds(str):
    print("开始异步"+str)
    time.sleep(60)
    print("睡眠60秒")

