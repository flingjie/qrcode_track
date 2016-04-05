# coding=utf8

import tornado.ioloop
import tornado.web
from tornado import gen
from settings import TEMPLATE_PATH, STATIC_PATH
from utils import gen_new_url
import qrcode
from io import BytesIO
import base64
from utils import analyse_client


class QRCodeGenerator(tornado.web.RequestHandler):
    def get(self):
        self.render("qrcode.html")

    def post(self):
        data = self.request.arguments['info']
        url = data[0].decode("utf-8")
        img = qrcode.make(gen_new_url(url))
        o = BytesIO()
        img.save(o, "JPEG")
        s = base64.b64encode(o.getvalue())
        self.set_header('Content-type', 'image/jpg')
        self.set_header('Content-length', len(s))
        self.write(s)


class TrackHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        url = self.get_argument("url", default="/")

        def do_track(callback):
            analyse_client(self.request.remote_ip, self.request.headers["user-agent"])
            callback()
        yield gen.Task(do_track)
        self.redirect(url)


def make_app():
    handlers = [
        (r"/track", TrackHandler),
        (r"/", QRCodeGenerator),
    ]
    return tornado.web.Application(handlers=handlers,
                                   template_path=TEMPLATE_PATH,
                                   static_path=STATIC_PATH)

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
