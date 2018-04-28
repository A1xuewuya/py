# -*- coding:utf-8 -*-
#
import hashlib
import MySqlCreater
import RedisCreater

# 接受用户输入
# name = raw_input("请输入用户名：")
# pwd = raw_input("请输入密码：")
#
name = "天空"
pwd = "123"

# 对密码加密
s1 = hashlib.sha1()
s1.update(pwd)
password = s1.hexdigest()

# 查询redis中是否存在
r = RedisCreater.RedisCreater()
temp = r.get(name)
if None == temp:
    # 根据用户名查询账户
    params = [name]
    sql = "select password from users where name=%s"
    db = MySqlCreater.MySqlCreater("10.10.120.12", 3306, "root", "root", "students")
    result = db.fetchone(sql, params)
    if None == result:
        print("用户名或密码错误")
    else:
        r.set(name, password)
        print("登录成功")