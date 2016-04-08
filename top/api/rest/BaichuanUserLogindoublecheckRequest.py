'''
Created by auto_sdk on 2015.06.10
'''
from top.api.base import RestApi
class BaichuanUserLogindoublecheckRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.name = None

	def getapiname(self):
		return 'taobao.baichuan.user.logindoublecheck'
