# coding=utf8
import os


BASE_PATH = os.path.realpath(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.join(BASE_PATH, "templates")
STATIC_PATH = os.path.join(BASE_PATH, "static")

HOST = "http://192.168.10.58:8000/track?url="

MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
DATABASE = "qrcode"

DEBUG = True
SECRET_KEY="keep#@!#secretabcdefgh#@!#@#@$%"
XSRF_FLAG = True
