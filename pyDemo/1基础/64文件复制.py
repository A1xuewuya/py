#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# 获取文件名
old_file_name = input("请输入要备份的文件名:")

# 打开文件和要备份的文件
f_read = open(old_file_name, "r")

pos = old_file_name.rfind(".")
new_file_name = old_file_name[:pos] + "[复件]" + old_file_name[pos:]
f_write = open(new_file_name, "w")

# 写入操作
while True:
    con = f_read.read(1024)
    if len(con) == 0:
        break
    f_write.write(con)

# 关闭文件
f_read.close()
f_write.close()