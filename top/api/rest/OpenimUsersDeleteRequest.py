'''
Created by auto_sdk on 2015.07.13
'''
from top.api.base import RestApi
class OpenimUsersDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.userids = None

	def getapiname(self):
		return 'taobao.openim.users.delete'
