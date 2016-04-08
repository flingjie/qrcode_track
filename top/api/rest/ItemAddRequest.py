'''
Created by auto_sdk on 2015.11.23
'''
from top.api.base import RestApi
class ItemAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.after_sale_id = None
		self.approve_status = None
		self.auction_point = None
		self.auto_fill = None
		self.auto_repost = None
		self.barcode = None
		self.change_prop = None
		self.chaoshi_extends_info = None
		self.cid = None
		self.cod_postage_id = None
		self.cpv_memo = None
		self.custom_made_type_id = None
		self.delivery_time_delivery_time = None
		self.delivery_time_delivery_time_type = None
		self.delivery_time_need_delivery_time = None
		self.desc = None
		self.desc_modules = None
		self.ems_fee = None
		self.express_fee = None
		self.features = None
		self.food_security_contact = None
		self.food_security_design_code = None
		self.food_security_factory = None
		self.food_security_factory_site = None
		self.food_security_food_additive = None
		self.food_security_health_product_no = None
		self.food_security_mix = None
		self.food_security_period = None
		self.food_security_plan_storage = None
		self.food_security_prd_license_no = None
		self.food_security_product_date_end = None
		self.food_security_product_date_start = None
		self.food_security_stock_date_end = None
		self.food_security_stock_date_start = None
		self.food_security_supplier = None
		self.freight_payer = None
		self.global_stock_country = None
		self.global_stock_delivery_place = None
		self.global_stock_tax_free_promise = None
		self.global_stock_type = None
		self.has_discount = None
		self.has_invoice = None
		self.has_showcase = None
		self.has_warranty = None
		self.ignorewarning = None
		self.image = None
		self.increment = None
		self.input_custom_cpv = None
		self.input_pids = None
		self.input_str = None
		self.is_3D = None
		self.is_ex = None
		self.is_lightning_consignment = None
		self.is_offline = None
		self.is_taobao = None
		self.is_xinpin = None
		self.item_size = None
		self.item_weight = None
		self.lang = None
		self.list_time = None
		self.locality_life_choose_logis = None
		self.locality_life_eticket = None
		self.locality_life_expirydate = None
		self.locality_life_merchant = None
		self.locality_life_network_id = None
		self.locality_life_obs = None
		self.locality_life_onsale_auto_refund_ratio = None
		self.locality_life_packageid = None
		self.locality_life_refund_ratio = None
		self.locality_life_refundmafee = None
		self.locality_life_verification = None
		self.locality_life_version = None
		self.location_city = None
		self.location_state = None
		self.ms_payment_price = None
		self.ms_payment_reference_price = None
		self.ms_payment_voucher_price = None
		self.newprepay = None
		self.num = None
		self.o2o_bind_service = None
		self.outer_id = None
		self.paimai_info_deposit = None
		self.paimai_info_interval = None
		self.paimai_info_mode = None
		self.paimai_info_reserve = None
		self.paimai_info_valid_hour = None
		self.paimai_info_valid_minute = None
		self.pic_path = None
		self.post_fee = None
		self.postage_id = None
		self.price = None
		self.product_id = None
		self.property_alias = None
		self.props = None
		self.qualification = None
		self.scenic_ticket_book_cost = None
		self.scenic_ticket_pay_way = None
		self.sell_point = None
		self.sell_promise = None
		self.seller_cids = None
		self.shape = None
		self.sku_barcode = None
		self.sku_delivery_times = None
		self.sku_hd_height = None
		self.sku_hd_lamp_quantity = None
		self.sku_hd_length = None
		self.sku_outer_ids = None
		self.sku_prices = None
		self.sku_properties = None
		self.sku_quantities = None
		self.sku_spec_ids = None
		self.spu_confirm = None
		self.stuff_status = None
		self.sub_stock = None
		self.support_custom_made = None
		self.title = None
		self.type = None
		self.valid_thru = None
		self.weight = None
		self.wireless_desc = None

	def getapiname(self):
		return 'taobao.item.add'

	def getMultipartParas(self):
		return ['image']

	def getTranslateParas(self):
		return {'food_security_stock_date_start':'food_security.stock_date_start','locality_life_choose_logis':'locality_life.choose_logis','food_security_plan_storage':'food_security.plan_storage','delivery_time_need_delivery_time':'delivery_time.need_delivery_time','ms_payment_reference_price':'ms_payment.reference_price','paimai_info_reserve':'paimai_info.reserve','food_security_factory':'food_security.factory','food_security_product_date_end':'food_security.product_date_end','location_state':'location.state','food_security_contact':'food_security.contact','locality_life_onsale_auto_refund_ratio':'locality_life.onsale_auto_refund_ratio','ms_payment_price':'ms_payment.price','locality_life_refundmafee':'locality_life.refundmafee','food_security_period':'food_security.period','food_security_stock_date_end':'food_security.stock_date_end','paimai_info_valid_minute':'paimai_info.valid_minute','locality_life_merchant':'locality_life.merchant','food_security_health_product_no':'food_security.health_product_no','paimai_info_mode':'paimai_info.mode','locality_life_obs':'locality_life.obs','ms_payment_voucher_price':'ms_payment.voucher_price','food_security_mix':'food_security.mix','locality_life_packageid':'locality_life.packageid','food_security_prd_license_no':'food_security.prd_license_no','paimai_info_valid_hour':'paimai_info.valid_hour','paimai_info_interval':'paimai_info.interval','location_city':'location.city','food_security_design_code':'food_security.design_code','paimai_info_deposit':'paimai_info.deposit','delivery_time_delivery_time_type':'delivery_time.delivery_time_type','locality_life_eticket':'locality_life.eticket','food_security_food_additive':'food_security.food_additive','locality_life_network_id':'locality_life.network_id','food_security_supplier':'food_security.supplier','food_security_factory_site':'food_security.factory_site','locality_life_version':'locality_life.version','food_security_product_date_start':'food_security.product_date_start','locality_life_expirydate':'locality_life.expirydate','locality_life_verification':'locality_life.verification','locality_life_refund_ratio':'locality_life.refund_ratio','delivery_time_delivery_time':'delivery_time.delivery_time'}
