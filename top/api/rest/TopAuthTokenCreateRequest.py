'''
Created by auto_sdk on 2015.08.20
'''
from top.api.base import RestApi
class TopAuthTokenCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.code = None

	def getapiname(self):
		return 'taobao.top.auth.token.create'
