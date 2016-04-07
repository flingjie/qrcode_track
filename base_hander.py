# coding=utf8
import tornado.web
from constants import USER_COLLECTION


class RequestHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        user_id = self.get_secure_cookie("user")
        if not user_id:
            return None
        return self.db[USER_COLLECTION].find_one({'phone': user_id})