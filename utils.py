# coding=utf8
from qqwry import QQwry
from ua_parser import user_agent_parser
from settings import TRACK_URL, STATISTIC_URL
from urllib import quote
from datetime import datetime
import json
from alidayu import AlibabaAliqinFcSmsNumSendRequest

q = QQwry('qqwry.dat')


def analyse_client(url, ip, ua, collection):
    visit = {
                'time': datetime.now(),
                'location': get_loc_from_ip(ip),
                'client': user_agent_parser.Parse(ua)
            }
    if collection.find_one({'url': url}):
        collection.update({'url': url}, {'$push': {'visit': visit}})
    else:
        data = {
            'url': url,
            'name': '',
            'visit': [visit]
        }
        collection.insert(data)


def get_loc_from_ip(ip):
    loc = q.ip_location(ip)
    return {
        'ip': ip,
        'loc': loc
    }


def add_http(url):
    if not url.startswith("http:"):
        url = "http://{}".format(url)
    return url


def gen_new_url(url):
    url = add_http(url)
    return "{}{}".format(TRACK_URL, quote(url))


def gen_statistic_url(url):
    url = add_http(url)
    return "{}{}".format(STATISTIC_URL, quote(url))


def send_msg(phone):
    req = AlibabaAliqinFcSmsNumSendRequest(u"23205423", u"7164357b0dd4b36699a4e433d4979313")
    req.extend = u"123456"
    req.sms_type = u"normal"
    req.sms_free_sign_name = u"阿里大鱼"
    params = {
        u"code": 123133,
        u"product": u"yiding"
    }
    req.sms_param = json.dumps(params)
    req.rec_num = phone
    req.sms_template_code = u"SMS_5410290"
    try:
        resp = req.getResponse()
        print(resp)
    except Exception,e:
        print(e)


