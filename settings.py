# coding=utf8
import os


BASE_PATH = os.path.realpath(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.join(BASE_PATH, "templates")
STATIC_PATH = os.path.join(BASE_PATH, "static")

HOST = "http://192.168.10.210:8000"
TRACK_URL = "{}/track?url=".format(HOST)
STATISTIC_URL = "{}/detail?url=".format(HOST)

MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
DATABASE = "qrcode"

DEBUG = True
SECRET_KEY="keep#@!#secretabcdefgh#@!#@#@$%"
XSRF_FLAG = True
