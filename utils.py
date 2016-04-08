# coding=utf8
from qqwry import QQwry
from datetime import datetime
from ua_parser import user_agent_parser
from settings import TRACK_URL, STATISTIC_URL
from urllib import quote


q = QQwry('qqwry.dat')


def analyse_client(ip, ua, collection):
    data = {}
    data['time'] = datetime.now()
    data['location'] = get_loc_from_ip(ip)
    data['client'] = user_agent_parser.Parse(ua)
    collection.insert(data)


def get_loc_from_ip(ip):
    loc, supplier = q.lookup(ip)
    return {
        'ip': ip,
        'loc': loc,
        'supplier': supplier
    }


def gen_new_url(url):
    if not url.startswith("http:"):
        url = "http://{}".format(url)
    return "{}{}".format(TRACK_URL, quote(url))


def gen_statistic_url(user_id):
    return "{}{}".format(STATISTIC_URL, quote(user_id))


