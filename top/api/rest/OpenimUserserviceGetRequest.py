'''
Created by auto_sdk on 2016.03.07
'''
from top.api.base import RestApi
class OpenimUserserviceGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.date = None
		self.page_no = None
		self.page_size = None

	def getapiname(self):
		return 'taobao.openim.userservice.get'
