'''
Created by auto_sdk on 2015.11.16
'''
from top.api.base import RestApi
class OpenAccountUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.param_list = None

	def getapiname(self):
		return 'taobao.open.account.update'
