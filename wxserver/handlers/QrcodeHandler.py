# -*- coding:utf-8 -*-
# 请求微信服务器生成带参数二维码给客户

import tornado.gen
import json

from BaseHandler import BaseHandler
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tools.AccessToken import Access_Token


class QrcodeHandeler(BaseHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        scene_id = self.get_argument("sid")
        try:
            access_token = yield Access_Token.get_access_token()
        except Exception as e:
            self.write("errmsg:%s" %e)
        else:
            url = "https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s" % access_token
            req_data = {"action_name": "QR_LIMIT_SCENE", "action_info": {"scene": {"scene_id": scene_id}}}
            req = HTTPRequest(
                url=url,
                method="POST",
                body=json.dumps(req_data),

            )
            client = AsyncHTTPClient()
            resp = yield client.fetch(req)
            resp_data = json.loads(resp.body)
            if "errcode" in resp_data:
                self.write("errmsg: get qrcode faild..")
            else:
                ticket = resp_data["ticket"]
                qrcode_url = resp_data["url"]
                self.write("<img src='https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s'>" % ticket)
                self.write("<p>%s</p>" % qrcode_url)