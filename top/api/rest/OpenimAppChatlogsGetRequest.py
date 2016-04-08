'''
Created by auto_sdk on 2015.09.25
'''
from top.api.base import RestApi
class OpenimAppChatlogsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.beg = None
		self.count = None
		self.end = None
		self.next = None

	def getapiname(self):
		return 'taobao.openim.app.chatlogs.get'
