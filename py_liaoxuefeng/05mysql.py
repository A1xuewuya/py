#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 导入mysql驱动
import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='test', use_unicode=True)
cursor = conn.cursor()

# 创建user表
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Jack'])
# print cursor.rowcount

# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print values

# 关闭Cursor和Connection:
cursor.close()
conn.close()
