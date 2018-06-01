#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
from django.db import models


class BookInfo(models.Model):
    btitle = models.CharField(max_length=32)
    bpub_date = models.DateTimeField(db_column='bpub_date')
    bread = models.IntegerField()
    bcomment = models.IntegerField()
    isDelete = models.BooleanField()


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    isDelete = models.BooleanField()
    book = models.ForeignKey('BookInfo')


class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    parea = models.ForeignKey('self', null=True, blank=True)
