# -*- coding:utf-8 -*-
#
import redis

redis_options = dict(
    host="10.10.120.12",
    port=6379,
    password="root",
)


class RedisCreater(object):
    def __init__(self):
        self.__redis = redis.StrictRedis(**redis_options)

    def set(self, key, value):
        self.__redis.set(key, value)

    def get(self, key):
        return self.__redis.get(key)


if __name__ == '__main__':
    redis = RedisCreater()
    redis.set("test00", "test00")
    temp = redis.get("test01")
    print(temp)
