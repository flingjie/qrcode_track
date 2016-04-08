'''
Created by auto_sdk on 2015.11.16
'''
from top.api.base import RestApi
class CloudpushPushRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.android_activity = None
		self.android_ext_parameters = None
		self.android_music = None
		self.android_open_type = None
		self.android_open_url = None
		self.anti_harass_duration = None
		self.anti_harass_start_time = None
		self.batch_number = None
		self.body = None
		self.device_type = None
		self.ios_badge = None
		self.ios_ext_parameters = None
		self.ios_music = None
		self.remind = None
		self.store_offline = None
		self.summery = None
		self.target = None
		self.target_value = None
		self.timeout = None
		self.title = None
		self.type = None

	def getapiname(self):
		return 'taobao.cloudpush.push'
