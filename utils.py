# coding=utf8
from qqwry import QQwry
from ua_parser import user_agent_parser
from settings import TRACK_URL, STATISTIC_URL
from urllib import quote
from datetime import datetime
import top.api

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
    req = top.api.OpenSmsSendvercodeRequest()
    req.set_app_info(top.appinfo("23205422", "3684dc7f4fe34862c13c8d3a86052e24"))
    req.send_ver_code_request = ""
    try:
        resp= req.getResponse()
        print(resp)
    except Exception,e:
        print(e)


