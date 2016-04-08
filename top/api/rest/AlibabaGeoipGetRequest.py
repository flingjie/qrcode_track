'''
Created by auto_sdk on 2015.08.20
'''
from top.api.base import RestApi
class AlibabaGeoipGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ip = None
		self.language = None

	def getapiname(self):
		return 'alibaba.geoip.get'
