# coding=utf8

import tornado.ioloop
import tornado.web
from tornado import gen
import os


class QRCodeGenerator(tornado.web.RequestHandler):
    def get(self):
        self.render("qrcode.html")


class StatisticHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        url = self.get_argument("url", default="/")

        def do_stuff(callback):
            for i in range(10):
                print(i)
            callback()
        yield gen.Task(do_stuff)
        self.redirect(url)


def make_app():
    template_path = os.path.join(os.path.dirname(__file__), "templates")
    static_path = os.path.join(os.path.dirname(__file__), "static")
    handlers = [
        (r"/", StatisticHandler),
        (r"/qr", QRCodeGenerator),
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_path}),
    ]
    return tornado.web.Application(handlers=handlers, template_path=template_path)

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
