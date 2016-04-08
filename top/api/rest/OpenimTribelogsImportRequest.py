'''
Created by auto_sdk on 2015.12.31
'''
from top.api.base import RestApi
class OpenimTribelogsImportRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.messages = None
		self.tribe_id = None

	def getapiname(self):
		return 'taobao.openim.tribelogs.import'
