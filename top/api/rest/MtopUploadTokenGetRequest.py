'''
Created by auto_sdk on 2015.05.25
'''
from top.api.base import RestApi
class MtopUploadTokenGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.param_upload_token_request = None

	def getapiname(self):
		return 'taobao.mtop.upload.token.get'
