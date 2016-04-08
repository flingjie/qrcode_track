'''
Created by auto_sdk on 2015.06.16
'''
from top.api.base import RestApi
class OpenimChatlogsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.begin = None
		self.count = None
		self.end = None
		self.next_key = None
		self.user1 = None
		self.user2 = None

	def getapiname(self):
		return 'taobao.openim.chatlogs.get'
