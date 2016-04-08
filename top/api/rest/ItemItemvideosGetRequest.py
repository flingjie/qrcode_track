'''
Created by auto_sdk on 2016.03.10
'''
from top.api.base import RestApi
class ItemItemvideosGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.item_id = None
		self.page_no = None
		self.page_size = None
		self.video_id = None

	def getapiname(self):
		return 'taobao.item.itemvideos.get'
