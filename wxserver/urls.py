# -*- coding:utf-8 -*-
#
from handlers import IndexHandler
from handlers import WechatHandler
from handlers import QrcodeHandler
from handlers import ProfileHandler

urls = [
    (r"/api/index", IndexHandler.IndexHandler),
    (r"/api/wechat", WechatHandler.WechatHandler),
    (r"/api/qrcode", QrcodeHandler.QrcodeHandeler),
    (r"/api/profile", ProfileHandler.ProfileHandler)
]