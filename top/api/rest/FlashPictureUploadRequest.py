'''
Created by auto_sdk on 2016.03.05
'''
from top.api.base import RestApi
class FlashPictureUploadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.image_input_title = None
		self.img = None
		self.nick = None
		self.title = None

	def getapiname(self):
		return 'taobao.flash.picture.upload'

	def getMultipartParas(self):
		return ['img']
