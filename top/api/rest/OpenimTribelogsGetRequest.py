'''
Created by auto_sdk on 2015.12.24
'''
from top.api.base import RestApi
class OpenimTribelogsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.begin = None
		self.count = None
		self.end = None
		self.next = None
		self.tribe_id = None

	def getapiname(self):
		return 'taobao.openim.tribelogs.get'
