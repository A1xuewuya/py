#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 


# 函数实现斐波那契数列
# def create_num():
#     a, b = 0, 1
#     for i in range(10):
#         print(b)
#         a, b = b, a + b

# create_num()

# 函数里面有yield则这个函数是生成器 生成器保存了一套算法
def create_num():
    a, b = 0, 1
    for i in range(10):
        yield b
        a, b = b, a + b


# a = create_num()  # 这一步返回生成器对象
# a1 = next(a)
# a2 = next(a)
# a3 = next(a)
# a4 = next(a)
# a5 = next(a)
for i in create_num():
    print(i)
