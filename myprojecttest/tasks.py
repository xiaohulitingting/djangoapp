#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from myprojecttest.celery import app
@app.task
def add(x, y):
    return x + y

@app.task
def test():
    print("------ceshi-----")
@app.task
def run_test_suit(ts_id):
    print("++++++++++++++++++++++++++++++++++++")
    print('jobs[ts_id=%s] running....' % ts_id)
    time.sleep(10.0)
    print('jobs[ts_id=%s] done' % ts_id)
    result = True
    return result