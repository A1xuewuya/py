#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 


class Home(object):
    def __init__(self, area, info, addr):
        self.area = area
        self.info = info
        self.addr = addr
        self.left_area = area
        self.contains_item = []

    def __str__(self):
        msg = "房子面积：%d，可用面积是:%s,房子户型：%s，房子地址：%s，" % (self.area, self.left_area, self.info, self.addr)
        msg += "当前房子里面有：%s" % (str(self.contains_item))
        return msg

    def add_item(self, item):
        self.left_area -= item.get_area()
        self.contains_item.append(item.get_name())


class Bed(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s占用的面积是:%d" % (self.name, self.area)

    def get_name(self):
        return self.name

    def get_area(self):
        return self.area


# 实例化房子对象
house = Home(135, "三室两厅", "北京朝阳区")

# 实例化家具床对象
bed1 = Bed("席梦思", 4)
bed2 = Bed("高级大床", 6)

# 给房子里面添加家具
house.add_item(bed1)
house.add_item(bed2)
print(house)
