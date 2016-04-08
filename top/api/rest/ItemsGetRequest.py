'''
Created by auto_sdk on 2015.06.11
'''
from top.api.base import RestApi
class ItemsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cid = None
		self.end_price = None
		self.end_score = None
		self.end_volume = None
		self.fields = None
		self.genuine_security = None
		self.is_3D = None
		self.is_cod = None
		self.is_mall = None
		self.is_prepay = None
		self.is_xinpin = None
		self.location_city = None
		self.location_state = None
		self.nicks = None
		self.one_station = None
		self.order_by = None
		self.page_no = None
		self.page_size = None
		self.post_free = None
		self.product_id = None
		self.promoted_service = None
		self.props = None
		self.q = None
		self.start_price = None
		self.start_score = None
		self.start_volume = None
		self.stuff_status = None
		self.ww_status = None

	def getapiname(self):
		return 'taobao.items.get'

	def getTranslateParas(self):
		return {'location_state':'location.state','location_city':'location.city'}
