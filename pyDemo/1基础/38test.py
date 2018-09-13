# -*- coding:utf-8 -*-

class Msg:
    def __init__(self):
        pass
    def __str__(self):
        return "发送信息类"
    def __sendMsg(self):
        print('发送信息成功')
    def sendMsg(self,money):
        if money > 10000:
            self.__sendMsg()
        else:
            print('发送信息失败')

if __name__ == '__main__':
    msg = Msg()
    msg.sendMsg(1)