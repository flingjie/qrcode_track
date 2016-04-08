'''
Created by auto_sdk on 2015.11.03
'''
from top.api.base import RestApi
class OpenimTrackGetdetailsRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.endtime = None
		self.prefix = None
		self.starttime = None
		self.uid = None

	def getapiname(self):
		return 'taobao.openim.track.getdetails'
