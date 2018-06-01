#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
import time
from celery import task

@task
def sayhello():
    print('hello ...')
    time.sleep(5)
    print('world ...')