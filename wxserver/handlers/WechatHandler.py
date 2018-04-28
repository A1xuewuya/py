# -*- coding:utf-8 -*-
#
import time
import hashlib
import xmltodict
from BaseHandler import BaseHandler
from configs.config_default import WECHAT_TOKEN


class WechatHandler(BaseHandler):
    def prepare(self):
        self.receive_data = xmltodict.parse(self.request.body)
        self.receive_data = self.receive_data["xml"]
        # 微信Token验证
        signature = self.get_argument("signature", "")
        timestamp = self.get_argument("timestamp", "")
        nonce = self.get_argument("nonce", "")
        # 将token、timestamp、nonce三个参数进行字典序排序
        temp = [WECHAT_TOKEN, timestamp, nonce]
        temp.sort()
        # 将三个参数字符串拼接成一个字符串进行sha1加密
        temp = "".join(temp)
        temp = hashlib.sha1(temp).hexdigest()
        # 开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
        if temp != signature:
            self.send_error(404)

    def get(self, *args, **kwargs):
        echostr = self.get_argument("echostr", "")
        self.write(echostr)

    def post(self, *args, **kwargs):
        msg_type = self.receive_data["MsgType"]
        if msg_type == "text":
            content = self.receive_data["Content"]
            resp_data = {
                "xml": {
                    "ToUserName": self.receive_data["FromUserName"],
                    "FromUserName": self.receive_data["ToUserName"],
                    "CreateTime": int(time.time()),
                    "MsgType": u"text",
                    "Content": u"客户端发送的文本消息..服务器做出的回应:%s" %content,
                }
            }
        elif msg_type == "event":
            if self.receive_data["Event"] == "subscribe":
                """用户关注事件"""
                resp_data = {
                    "xml": {
                        "ToUserName": self.receive_data["FromUserName"],
                        "FromUserName": self.receive_data["ToUserName"],
                        "CreateTime": int(time.time()),
                        "MsgType": u"text",
                        "Content": u"感谢关注..服务器发送的消息.. ",
                    }
                }
                if "EventKey" in self.receive_data["EventKey"]:
                    event_key = self.receive_data["EventKey"]
                    scene_id = event_key[8:]
                    resp_data["xml"]["Content"] = u"感谢关注,场景值:%s" % scene_id
            if self.receive_data["Event"] == "SCAN":
                scene_id = self.receive_data["EventKey"]
                resp_data = {
                    "xml": {
                        "ToUserName": self.receive_data["FromUserName"],
                        "FromUserName": self.receive_data["ToUserName"],
                        "CreateTime": int(time.time()),
                        "MsgType": u"text",
                        "Content": u"你扫描的是:%s" % scene_id,
                    }
                }

        else:
            resp_data = {
                "xml": {
                    "ToUserName": self.receive_data["FromUserName"],
                    "FromUserName": self.receive_data["ToUserName"],
                    "CreateTime": int(time.time()),
                    "MsgType": u"text",
                    "Content": u"客户端发送的不是文本消息..服务器做出的回应..",
                }
            }
        resp_data = xmltodict.unparse(resp_data)
        self.write(resp_data)
