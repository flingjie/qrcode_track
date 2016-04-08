'''
Created by auto_sdk on 2015.07.01
'''
from top.api.base import RestApi
class OpenimIoscertProductionSetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cert = None
		self.password = None

	def getapiname(self):
		return 'taobao.openim.ioscert.production.set'
