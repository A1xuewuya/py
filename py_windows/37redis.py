# -*- coding:utf-8 -*-
#
import redis

redis_options = dict(
    host="10.10.120.12",
    port=6379,
    password="root",
)

# 连接redis
r = redis.StrictRedis(**redis_options)

# 写
"""
pipe = r.pipeline()
pipe.set("test00", "test00")
pipe.set("test01", "test01")
pipe.execute()
"""
# 读取
try:
    temp = r.get("test00")
    print(temp)
except Exception as e:
    print(e)
