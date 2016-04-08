'''
Created by auto_sdk on 2015.08.06
'''
from top.api.base import RestApi
class DeliverySendRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.company_code = None
		self.feature = None
		self.fetcher_address = None
		self.fetcher_area_id = None
		self.fetcher_mobile = None
		self.fetcher_name = None
		self.fetcher_phone = None
		self.fetcher_zip = None
		self.memo = None
		self.order_type = None
		self.out_sid = None
		self.seller_address = None
		self.seller_area_id = None
		self.seller_mobile = None
		self.seller_name = None
		self.seller_phone = None
		self.seller_zip = None
		self.tid = None

	def getapiname(self):
		return 'taobao.delivery.send'
