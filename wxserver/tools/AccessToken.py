# -*- coding:utf-8 -*-
# access_token辅助类
import time
import json
import tornado.gen
from tornado.httpclient import AsyncHTTPClient
from configs.config_default import WECHAT_APP_ID
from configs.config_default import WECHAT_APP_SECRET


class Access_Token(object):
    _access_token = None
    _create_time = 0
    _expires_in = 0

    @classmethod
    @tornado.gen.coroutine
    def get_access_token(cls):
        if int(time.time()) - cls._create_time > (cls._expires_in - 200):
            # 向微信服务器更新access_token
            yield cls.update_access_token()
            raise tornado.gen.Return(cls._access_token)
        else:
            raise tornado.gen.Return(cls._access_token)

    @classmethod
    @tornado.gen.coroutine
    def update_access_token(cls):
        client = AsyncHTTPClient()
        url = "https://api.weixin.qq.com/cgi-bin/token?" \
              "grant_type=client_credential&appid=%s&secret=%s" % (WECHAT_APP_ID, WECHAT_APP_SECRET)
        resp = yield client.fetch(url)
        resp_data = json.loads(resp.body)
        print(resp_data)
        if "errcode" in resp_data:
            raise Exception("wechat server error")
        else:
            cls._access_token = resp_data["access_token"]
            cls._expires_in = resp_data["expires_in"]
            cls._create_time = time.time()

if __name__ == '__main__':
    resp = Access_Token.get_access_token()