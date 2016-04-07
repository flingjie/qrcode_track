# coding=utf8

import tornado.ioloop
import tornado.web
from pymongo import MongoClient
from handlers import QRCodeGenerator, TrackHandler, RegisterHandler, LoginHandler, StatisticHandler
from settings import *


def make_app():
    handlers = [
        (r"/track", TrackHandler),
        (r"/", QRCodeGenerator),
        (r"/register", RegisterHandler),
        (r"/login", LoginHandler),
        (r"/statistic", StatisticHandler),
    ]
    client = MongoClient(MONGODB_HOST, MONGODB_PORT)
    db = client[DATABASE]
    app = tornado.web.Application(handlers=handlers,
                                  template_path=TEMPLATE_PATH,
                                  login_url="/login",
                                  static_path=STATIC_PATH,
                                  cookie_secret=SECRET_KEY,
                                  xsrf_cookies=XSRF_FLAG,
                                  debug=DEBUG)
    app.db = db
    return app


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
