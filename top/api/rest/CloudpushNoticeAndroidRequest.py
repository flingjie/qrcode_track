'''
Created by auto_sdk on 2015.06.08
'''
from top.api.base import RestApi
class CloudpushNoticeAndroidRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.summary = None
		self.target = None
		self.target_value = None
		self.title = None

	def getapiname(self):
		return 'taobao.cloudpush.notice.android'
