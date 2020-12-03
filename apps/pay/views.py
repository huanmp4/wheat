from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
import hashlib, time
import random
from . import app01 as settings
import requests

#他们的
appid1 = "wx4df25ad915c7b761"
secret1 = "e2b34a530f0176206ca9bd6d45a28ca0"
openid = "oudwR5YvqscjRxKI8jsA0BOQpXu0"

url = "https://api.mch.weixin.qq.com/pay/unifiedorder"
appid = "wx4df25ad915c7b761"
mch_id = "1601649349"

# mch_secrit = "JCQ12345678900987654321wjy123456"
mch_secrit = "0E59D14A5FBFF881C99B2EBCDAC38dcd"
body = 'test'

def index(request):
  pass

class Pay(APIView):
  def post(self, request):
    param = request.data
    if param.get("openid"):  # 从redis中拿到小程序端login_key所对应得opendi&session_key值
      # openid, session_key = cache.get(param.get("login_key")).split("&")
      # openid= cache.get(request.data.get("openid"))
      openid= request.data.get("openid")
      print("openid:",openid)
      self.openid = openid
      # 获取用户IP
      # 1.如果是Nginx做的负载就要HTTP_X_FORWARDED_FOR
      if request.META.get('HTTP_X_FORWARDED_FOR'):
        self.ip = request.META['HTTP_X_FORWARDED_FOR']
      else:
        # 2.如果没有用Nginx就用REMOTE_ADDR
        self.ip = request.META['REMOTE_ADDR']
      # 调用 生成商户订单 方法
      data = self.pay()
      return Response({"code": 200, "msg": "ok", "data": data})
    else:
      return Response({"code": 200, "msg": "缺少参数"})

  # 生成随机字符串
  def get_str(self):
    str_all = "1234567890abcdefghjklmasdwery"  # 注意 开发活动功能时, 去掉1,i,0,o
    nonce_str = "".join(random.sample(str_all, 20))
    return nonce_str

  # 生成订单号
  def get_order(self):
    order_id = str(time.strftime("%Y%m%d%H%M%S"))
    return order_id


  # 处理返回预付单方法
  def xml_to_dict(self, data):
    import xml.etree.ElementTree as ET
    xml_dict = {}
    data_dic = ET.fromstring(data)
    for item in data_dic:
      xml_dict[item.tag] = item.text
    return xml_dict


  # 获取sign签名方法
  def get_sign(self):
    data_dic = {
      "nonce_str": self.nonce_str,
      "out_trade_no": self.out_trade_no,
      "spbill_create_ip": self.ip,
      "notify_url": self.notify_url,
      "openid": self.openid,
      "body": self.body,
      "trade_type": "JSAPI",
      "appid": self.appid,
      "total_fee": self.total_fee,
      "mch_id": self.mch_id
    }
    data_dic_backup = {
      "appId": self.appid,
      "mch_id": self.mch_id,
      "device_info": "iphone8_plus",
      "body": self.body,
      "nonce_str": self.nonce_str,
      "out_trade_no": self.out_trade_no,
      "spbill_create_ip": self.ip,
      "notify_url": self.notify_url,
      "openid": self.openid,
      "trade_type": "JSAPI",
      "total_fee": self.total_fee
    }

    sign_str = "&".join([f"{k}={data_dic[k]}" for k in sorted(data_dic)])
    sign_str = f"{sign_str}&key={settings.pay_apikey}"
    print("sign_str:",sign_str)
    md5 = hashlib.md5()
    md5.update(sign_str.encode("utf-8"))
    return md5.hexdigest().upper()


  # 1.生成商户订单 提供 支付统一下单 所需参数
  def pay(self):
    self.appid = settings.AppId  # appid 微信分配的小程序ID
    self.mch_id = settings.pay_mchid  # mch_id 微信分配的商户号
    self.nonce_str = self.get_str()  # 随机字符串
    self.body = "商品名"  # 商品名一般由小程序端传到后端
    self.out_trade_no = self.get_order()  # 订单号
    self.total_fee = 1  # 订单总金额
    self.spbill_create_ip = self.ip  # 用户ip
    self.notify_url = "http://vs6688.com:81/pay/receive"  # 异步接收微信支付结果通知的回调地址
    self.trade_type = "JSAPI"  # 固定写法
    self.sign = self.get_sign()  # 获取sign 签名

    data = f'''
      <xml>
        <appid>{self.appid}</appid>
        <body>{ self.body}</body>
        <mch_id>{self.mch_id}</mch_id>
        <nonce_str>{self.nonce_str}</nonce_str>
        <notify_url>{self.notify_url}</notify_url>
        <openid>{self.openid}</openid>
        <out_trade_no>{self.out_trade_no}</out_trade_no>
        <spbill_create_ip>{self.spbill_create_ip}</spbill_create_ip>
        <total_fee>{self.total_fee}</total_fee>
        <trade_type>{self.trade_type}</trade_type>
        <sign>{self.sign}</sign>
      </xml>
        '''
    # data2 = f'''
    #   <xml>
    #    <appid>wx2421b1c4370ec43b</appid>
    #    <attach>支付测试</attach>
    #    <body>JSAPI支付测试</body>
    #    <mch_id>10000100</mch_id>
    #    <detail><![CDATA[{ "goods_detail":[ { "goods_id":"iphone6s_16G", "wxpay_goods_id":"1001", "goods_name":"iPhone6s 16G", "quantity":1, "price":528800, "goods_category":"123456", "body":"苹果手机" }, { "goods_id":"iphone6s_32G", "wxpay_goods_id":"1002", "goods_name":"iPhone6s 32G", "quantity":1, "price":608800, "goods_category":"123789", "body":"苹果手机" } ] }]]></detail>
    #    <nonce_str>1add1a30ac87aa2db72f57a2375d8fec</nonce_str>
    #    <notify_url>http://wxpay.wxutil.com/pub_v2/pay/notify.v2.php</notify_url>
    #    <openid>oUpF8uMuAJO_M2pxb1Q9zNjWeS6o</openid>
    #    <out_trade_no>1415659990</out_trade_no>
    #    <spbill_create_ip>14.23.150.211</spbill_create_ip>
    #    <total_fee>1</total_fee>
    #    <trade_type>JSAPI</trade_type>
    #    <sign>0CB01533B8C1EF103065174F50BCA001</sign>
    # </xml>
    #   '''
    # data3 = f'''
    #   <xml>
    #      <appid><![CDATA[{self.appid}]]></appid>
    #      <body><![CDATA[{ self.body}]]></body>
    #      <mch_id><![CDATA[{self.mch_id}]]></mch_id>
    #      <nonce_str><![CDATA[{self.nonce_str}]]></nonce_str>
    #      <notify_url><![CDATA[{self.notify_url}]]></notify_url>
    #      <openid><![CDATA[{self.openid}]]></openid>
    #      <out_trade_no><![CDATA[{self.out_trade_no}]]></out_trade_no>
    #      <spbill_create_ip><![CDATA[{self.spbill_create_ip}]]></spbill_create_ip>
    #      <total_fee><![CDATA[{self.total_fee}]]></total_fee>
    #      <trade_type><![CDATA[{self.trade_type}]]></trade_type>
    #      <sign>{self.sign}</sign>
    #   </xml>
    #   '''
    # data4 = f'''
    # <xml>
    #   <detail><![CDATA[{ "goods_detail":[ { "goods_id":"iphone6s_16G", "wxpay_goods_id":"1001", "goods_name":"iPhone6s 16G", "quantity":1, "price":528800, "goods_category":"123456", "body":"苹果手机" }, { "goods_id":"iphone6s_32G", "wxpay_goods_id":"1002", "goods_name":"iPhone6s 32G", "quantity":1, "price":608800, "goods_category":"123789", "body":"苹果手机" } ] }]]></detail>
    #   <nonce_str>1add1a30ac87aa2db72f57a2375d8fec</nonce_str>
    #   <appid><![CDATA[wx4df25ad915c7b761]]></appid>
    #   <body><![CDATA[test]]></body>
    #   <mch_id><![CDATA[1601649349]]></mch_id>
    #   <nonce_str><![CDATA[5K8264ILTKCH16CQ2502SI8ZNMTM67VS]]></nonce_str>
    #   <notify_url><![CDATA[http://www.baidu.com]]></notify_url>
    #   <openid><![CDATA[oudwR5YvqscjRxKI8jsA0BOQpXu0]]></openid>
    #   <out_trade_no><![CDATA[20201124211559]]></out_trade_no>
    #   <spbill_create_ip><![CDATA[127.0.0.1]]></spbill_create_ip>
    #   <total_fee><![CDATA[1]]></total_fee>
    #   <trade_type><![CDATA[JSAPI]]></trade_type>
    #   <sign>6C66AA022F4CCE0F81D316B9C911505C</sign>
    # </xml>
    # '''
    print("统一下单DATA:",data)

    # 2.支付统一下单接口
    url = "https://api.mch.weixin.qq.com/pay/unifiedorder"
    # 3.返回预付单信息
    response = requests.post(url, data.encode("utf-8"), headers={"content-type": "application/xml"})
    res_data = self.xml_to_dict(response.content)
    print("统一订单回调:", response)
    print("统一订单回调:", res_data)
    data = self.two_sign(res_data["prepay_id"])  # prepay_id 预支付订单回话标识
    return data

  # 4.将组合数据再次签名
  def two_sign(self, prepay_id):
    timeStamp = str(int(time.time()))
    nonceStr = self.get_str()
    data_dict = {
      "appId": settings.AppId,
      "timeStamp": timeStamp,
      "nonceStr": nonceStr,
      "package": f"prepay_id={prepay_id}",
      "signType": "MD5"
    }
    sign_str = "&".join([f"{k}={data_dict[k]}" for k in sorted(data_dict)])
    sign_str = f"{sign_str}&key={settings.pay_apikey}"
    md5 = hashlib.md5()
    md5.update(sign_str.encode("utf-8"))
    sign = md5.hexdigest().upper()
    data_dict["paySign"] = sign
    data_dict.pop("appId")
    # 5.返回支付参数到小程序端,小程序端获取所需参数向微信服务器发送 调起支付 方法
    print("二次签名：",data_dict)
    return data_dict

def receive(request):
  print("成功")