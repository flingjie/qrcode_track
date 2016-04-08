'''
Created by auto_sdk on 2015.06.17
'''
from top.api.base import RestApi
class OpenimRelationsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.beg_date = None
		self.end_date = None
		self.user = None

	def getapiname(self):
		return 'taobao.openim.relations.get'
