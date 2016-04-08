'''
Created by auto_sdk on 2015.12.04
'''
from top.api.base import RestApi
class TimeGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'taobao.time.get'
