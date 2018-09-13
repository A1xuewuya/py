#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
import os

folder_name = input("请输入要重命名文件夹内容的名字：")
os.chdir(folder_name)

file_list = os.listdir()
for v in file_list:
    old_file_name = v
    new_file_name = "[你好世界]" + v
    os.rename(old_file_name, new_file_name)
