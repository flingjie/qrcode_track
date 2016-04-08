'''
Created by auto_sdk on 2015.08.28
'''
from top.api.base import RestApi
class OpenSmsCheckvercodeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.check_ver_code_request = None

	def getapiname(self):
		return 'taobao.open.sms.checkvercode'
