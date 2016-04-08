'''
Created by auto_sdk on 2015.08.10
'''
from top.api.base import RestApi
class OpenAccountSearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.query = None

	def getapiname(self):
		return 'taobao.open.account.search'
