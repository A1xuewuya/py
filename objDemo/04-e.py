#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Home:
    def __init__(self, area, info, addr):
        self.area = area
        self.info = info
        self.addr = addr
        self.left_area = area
        self.other = []

    def __str__(self):
        msg = '房子面积：%d,剩余面积：%d,信息：%s,地址：%s,家具有:%s' % (self.area, self.left_area,self.info, self.addr, str(self.other))
        return msg

    def add_item(self, instance):
        self.left_area -= instance.get_area()
        self.other.append(instance.get_other)


class Bed:
    def __init__(self, area, info):
        self.area = area
        self.info = info

    def __str__(self):
        pass

    def get_area(self):
        return self.area

    def get_other(self):
        return self.info


if __name__ == '__main__':
    fangzi = Home(135, '三室两厅', '北京海淀区666号')
    bed1 = Bed(4, '豪华双人')
    fangzi.add_item(bed1)
    print fangzi

