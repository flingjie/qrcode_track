'''
Created by auto_sdk on 2016.03.10
'''
from top.api.base import RestApi
class MediaCategoryUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.media_category_id = None
		self.media_category_name = None

	def getapiname(self):
		return 'taobao.media.category.update'
