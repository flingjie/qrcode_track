'''
Created by auto_sdk on 2015.05.08
'''
from top.api.base import RestApi
class ItemImgDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.is_sixth_pic = None
		self.num_iid = None

	def getapiname(self):
		return 'taobao.item.img.delete'
