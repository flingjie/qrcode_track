# coding=utf8
import base64
from io import BytesIO
import bcrypt
import qrcode
import tornado.web
from tornado import gen
from base_hander import RequestHandler
from constants import *
from utils import gen_new_url, analyse_client, gen_statistic_url
from PIL import Image


class RegisterHandler(RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        self.render("register.html")

    @tornado.gen.coroutine
    def post(self):
        arg0 = self.request.arguments.get('phone')
        arg1 = self.request.arguments.get('pwd')

        if arg0 and arg1:
            phone = arg0[0]
            password = arg1[0]
            users = self.db['user']
            user = users.find_one({"phone": phone})
            if user:
                self.write({
                    "status": ERROR,
                    "msg": "手机号已被使用"
                })
            else:
                hashed_pass = bcrypt.hashpw(password, bcrypt.gensalt())
                data = {
                    "phone": phone,
                    "password": hashed_pass,
                    "qrcode": []
                }
                users.insert(data)
                self.write({
                    "status": OK
                })
        else:
            self.write({
                "status": ERROR,
                "msg": "注册信息缺失"
            })


class LoginHandler(RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        self.render("login.html")

    @tornado.gen.coroutine
    def post(self):
        users = self.db[USER_COLLECTION]
        arg0 = self.request.arguments.get('phone')
        arg1 = self.request.arguments.get('pwd')

        if arg0 and arg1:
            phone = arg0[0]
            password = arg1[0]
            user = users.find_one({
                'phone': phone
            })
            if user and phone and password and bcrypt.hashpw(password, user['password'].encode("utf-8")) == user['password']:
                self.set_secure_cookie("user", user["phone"])
            else:
                self.write({
                    "status": ERROR,
                    "msg": "用户名或密码错误"
                })
        else:
            self.write({
                "status": ERROR,
                "msg": "请输入用户名和密码"
            })


class LogoutHandler(RequestHandler):
    @tornado.web.authenticated
    @tornado.gen.coroutine
    def get(self):
        self.clear_cookie("user")
        self.redirect("/login")


class QRCodeGenerator(RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        self.render("qrcode.html")

    @tornado.gen.coroutine
    def post(self):
        post_type = self.request.arguments.get('type')[0]
        if int(post_type) == LINK_TYPE:
            data = self.request.arguments.get('info')[0]
            url = data.decode("utf-8")
        else:
            b64img = self.request.arguments.get('image')[0]
            img = BytesIO(base64.b64decode(b64img))
            scanner = zbar.ImageScanner()
            scanner.parse_config('enable')
            pil = Image.open(img).convert('L')
            width, height = pil.size
            raw = pil.tobytes()
            image = zbar.Image(width, height, 'Y800', raw)
            scanner.scan(image)
            for symbol in image:
                print(symbol.type)
                print(symbol.data)
                url = symbol.data
        img = qrcode.make(gen_new_url(url))
        o = BytesIO()
        img.save(o, "JPEG")
        s = base64.b64encode(o.getvalue())

        # todo
        img = qrcode.make(gen_statistic_url("test"))
        o = BytesIO()
        img.save(o, "JPEG")
        s2 = base64.b64encode(o.getvalue())

        self.write({
            "qrcode": s.decode('utf-8'),
            "statistic": s2.decode('utf-8')
        })


class TrackHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        url = self.get_argument("url", default="/")

        def do_track(callback):
            analyse_client(self.request.remote_ip,
                           self.request.headers["user-agent"],
                           self.db[STATISTIC_COLLECTION])
            callback()
        yield gen.Task(do_track)
        self.redirect(url)


class StatisticHandler(RequestHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self):
        self.render("statistic.html")