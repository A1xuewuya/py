# -*- coding:utf-8 -*-
#
import MySQLdb

mysql_options = dict(
    host="10.10.120.12",
    port=3306,
    db="students",
    user="root",
    passwd="root",
)

try:
    # 打开数据库连接
    db = MySQLdb.connect(**mysql_options)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("select version()")
    # 使用 fetchone() 方法获取一条数据
    res = cursor.fetchone()
    print(res)
except Exception as e:
    print(e)
else:
    cursor.close()
    db.close()

