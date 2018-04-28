# -*- coding:utf-8 -*-
#
import json
import urllib
import tornado.gen
from BaseHandler import BaseHandler
from tornado.httpclient import AsyncHTTPClient
from configs.config_default import WECHAT_APP_ID,WECHAT_APP_SECRET


class ProfileHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        code = self.get_argument("code", "")

        client = AsyncHTTPClient()
        url = "https://api.weixin.qq.com/sns/oauth2/access_token?" \
              "appid=%s&secret=%s&code=%s" \
              "&grant_type=authorization_code" % (WECHAT_APP_ID, WECHAT_APP_SECRET, code)
        resp = yield client.fetch(url)
        resp_data = json.loads(resp.body)
        access_token = resp_data.get("access_token")
        open_id = resp_data.get("openid")
        if "errcode" in resp_data:
            self.write("error ..")
        else:
            url = "https://api.weixin.qq.com/sns/userinfo?" \
                  "access_token=%s&openid=%s&lang=zh_CN" % (access_token, open_id)
            resp = yield client.fetch(url)
            # resp_data = json.loads(resp.body)
            if "errcode" in resp_data:
                self.write("error..")
            else:
                self.write(resp)