'''
Created by auto_sdk on 2015.09.23
'''
from top.api.base import RestApi
class OpenimImmsgPushRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.immsg = None

	def getapiname(self):
		return 'taobao.openim.immsg.push'
