'''
Created by auto_sdk on 2016.01.28
'''
from top.api.base import RestApi
class OpenimCustmsgPushRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.custmsg = None

	def getapiname(self):
		return 'taobao.openim.custmsg.push'
