# -*- coding:utf-8 -*-
from django.contrib import admin
from models import *


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bread', 'bpub_date']


admin.site.register(BookInfo, BookInfoAdmin)

# 两种办法注册后台
# @admin.register(BookInfo)
# class BookInfoAdmin(admin.ModelAdmin):
#     list_display = ['id', 'btitle', 'bread', 'bpub_date']
