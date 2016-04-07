# coding=utf8
import base64
from io import BytesIO
import bcrypt
import qrcode
import tornado.web
from tornado import gen
from base_hander import RequestHandler
from constants import OK, ERROR, USER_COLLECTION, STATISTIC_COLLECTION
from utils import gen_new_url, analyse_client


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
            if phone and password and bcrypt.hashpw(password, user['password']) == user['password']:
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
        data = self.request.arguments.get('info')[0]
        url = data.decode("utf-8")
        img = qrcode.make(gen_new_url(url))
        o = BytesIO()
        img.save(o, "JPEG")
        s = base64.b64encode(o.getvalue())
        self.set_header('Content-type', 'image/jpg')
        self.set_header('Content-length', len(s))
        self.write(s)


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