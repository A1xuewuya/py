# -*- coding:utf-8 -*-
# 数据库操作
import MySQLdb
"""
try:
    # 创建数据库连接对象
    conn = MySQLdb.connect(
        host="10.10.120.12",
        port=3306,
        user="root",
        passwd="root",
        db="students",
        charset="utf8",
    )
    # 创建一个游标对象
    cursor = conn.cursor()

    # 增加
    # sql = "insert into students(name) values('王天')"
    # 删除
    # sql = "delete from students where stuid=3"
    # 修改
    # sql = "update students set gender=1 where name='学无涯'"
    # 查询
    sql = "select * from students"
    cursor.execute(sql)

    # 事务提交
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
except Exception as e:
    print(e)
"""

# 防止sql注入
try:
    conn = MySQLdb.connect(
        host="10.10.120.12",
        port=3306,
        user="root",
        passwd="root",
        db="students",
        charset="utf8"
    )
    cursor = conn.cursor()
    name = raw_input("请输入用户名:")
    params=[name]
    sql = "insert into students(name) values(%s)"
    cursor.execute(sql, params)
    conn.commit()
    cursor.close()
    conn.close()
except Exception as e:
    print(e)
