'''
Created by auto_sdk on 2015.10.22
'''
from top.api.base import RestApi
class OpenimTribeCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.members = None
		self.notice = None
		self.tribe_name = None
		self.tribe_type = None
		self.user = None

	def getapiname(self):
		return 'taobao.openim.tribe.create'
