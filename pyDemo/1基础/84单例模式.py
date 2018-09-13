#!/usr/bin/env python
# 单例模式


class Person(object):
    __instance = None
    __init_flag = False

    def __str__(self):
        pass

    def __init__(self, name):
        if not Person.__init_flag:
            print("初始化方法... %s " % name)
            self.name = name
            Person.__init_flag = True

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance


xwy = Person("你好")
wt = Person("世界")

print(id(xwy))
print(id(wt))
