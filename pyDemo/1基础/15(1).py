#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
print("="*20)
print("名字管理系统V1.0")
print("="*20)
print("请输入操作序号:")
print("1:添加名称")
print("2:删除名字")
print("3:修改名字")
print("4:查询名字")
print("5:结束系统")
print("="*20)

# 名字存储列表
names_list = []

while True:
    option_num = int(input("请输入操作序号:"))
    if option_num == 1:
        new_name = input("请输入要添加名字:")
        names_list.append(new_name)
        print("添加成功！")
    elif option_num == 2:
        del_name = input("请输入要删除的名字:")
        if del_name in names_list:
            names_list.remove(del_name)
            print("删除成功！")
    elif option_num == 3:
        # update_name = input("请输入要更新的名字")
        # if update_name in names_list:
            pass
    elif option_num == 4:
        find_name = input("请输入要查询的名字:")
        if find_name in names_list:
            print("名字存在")
        else:
            print("名字不存在")
    elif option_num == 5:
        break