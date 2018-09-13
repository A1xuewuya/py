#!/usr/bin/env python
# -*- coding:utf-8 -*-
#


class Person(object):
    """人类"""

    def __init__(self, name):
        self.name = name
        self.gun = None
        self.hp = 100

    def anzhuang_danjia(self, danjia, zidan):
        # 将子弹安装到弹匣中
        danjia.add_zidan(zidan)

    def anzhuang_gun(self, jiatelin, danjia):
        # 将弹夹安装到枪中
        jiatelin.add_danjia(danjia)

    def naqiang(self, gun):
        self.gun = gun

    def koubanji(self, diren):
        """让枪打敌人"""
        self.gun.fire(diren)

    def diaoxue(self, sha_shang_li):
        self.hp -= sha_shang_li


class Gun(object):
    """枪类"""

    def __init__(self, name):
        self.name = name
        self.danjia = None

    def add_danjia(self, danjia):
        self.danjia = danjia

    def fire(self, diren):
        # 枪从弹夹中获取一发子弹，打敌人，敌人血量减少
        # 先从弹夹中取子弹
        zidan = self.danjia.tanchu_zidan()
        if zidan:
            # 子弹打中敌人
            zidan.dazhong(diren)
        else:
            print("弹夹中没有子弹了...")


class Danjia(object):
    """弹夹类"""

    def __init__(self, max_num):
        self.max_num = max_num
        self.zidan_list = []

    def __str__(self):
        return "弹夹信息:%d/%d" % (len(self.zidan_list), self.max_num)

    def add_zidan(self, zidan):
        self.zidan_list.append(zidan)

    def tanchu_zidan(self):
        # 弹出最上面的那颗子弹
        if self.zidan_list:
            return self.zidan_list.pop()
        return None


class Zidan(object):
    """子弹类"""

    def __init__(self, sha_shang_li):
        self.sha_shang_li = sha_shang_li

    def dazhong(self, diren):
        # 让敌人掉血一颗子弹的威力
        diren.diaoxue(self.sha_shang_li)


def main():
    # 1. 创建一个人对象
    laowang = Person("老王")

    # 2. 创建一个枪类
    jiatelin = Gun("加特林")

    # 3. 创建一个弹夹对象
    danjia = Danjia(20)

    # 4. 创建一个子弹对象
    # zidan = Zidan(10)

    # 5. 老王安装子弹到弹夹中 这是创建的一个子弹对象放入了15次
    for i in range(15):
        zidan = Zidan(10)
        laowang.anzhuang_danjia(danjia, zidan)

    # 6. 老王安装弹夹到枪中
    laowang.anzhuang_gun(jiatelin, danjia)

    # 7. 老王拿枪
    laowang.naqiang(jiatelin)

    # 8. 创建敌人
    laosong = Person("老宋")

    # 9. 老王开枪打老宋
    laowang.koubanji(laosong)


if __name__ == '__main__':
    main()
