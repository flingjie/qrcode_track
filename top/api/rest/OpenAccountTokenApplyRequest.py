'''
Created by auto_sdk on 2015.06.30
'''
from top.api.base import RestApi
class OpenAccountTokenApplyRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.isv_account_id = None
		self.login_state_expire_in = None
		self.open_account_id = None
		self.token_timestamp = None
		self.uuid = None

	def getapiname(self):
		return 'taobao.open.account.token.apply'
