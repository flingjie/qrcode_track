'''
Created by auto_sdk on 2015.12.28
'''
from top.api.base import RestApi
class OpenimTribeSetmembernickRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.member = None
		self.nick = None
		self.tribe_id = None
		self.user = None

	def getapiname(self):
		return 'taobao.openim.tribe.setmembernick'
