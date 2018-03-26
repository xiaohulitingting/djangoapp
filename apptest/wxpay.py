'''
流程简介
网页内调起微信支付需要一个微信统一下单生成的订单号(prepay_id)
调用微信的统一下单接口需要一个用户在商户下的唯一标示(openid)
获取openid需要code参数加上AppID和AppSecret等，通过API换取access_token(openid)
其中code又需要通过页面跳转来获取, 需要appid和重定向url(可以带有你自己的参数, 会原样返回)
那么开发思路便是一步步回朔了.https://www.cnblogs.com/wancy86/p/wcpay.html
'''
import apptest.request as request
import hashlib
from myprojecttest import settings
import uuid
import json,time,datetime
import xmltodict

'''
1. 获取code
用户点击按钮跳转到微信授权页, 微信处理完后重定向到redirect_uri, 并给我们加上code=xxx的参数, 这个code就是我们需要的

    $('#buy').click(function() {
        var param = {
            appid: 'wx53c18f32ad626eb8',
            redirect_uri: 'https://www.huizeguoxue.com/wcpay/pay.html',
            response_type: 'code',
            scope: 'snsapi_base',
            state: '1'
        }
        window.location.href = 'https://open.weixin.qq.com/connect/oauth2/authorize?' + $.param(param);
    })
'''
#2.获取openid
@classmethod
def getOpenID(kwargs):
    param = {
        'code': kwargs['code'],
        'appid':kwargs['appid'],
        'secret': kwargs['secret'],
        'grant_type': 'authorization_code',
    }

    # 通过code获取access_token
    openIdUrl = 'https://api.weixin.qq.com/sns/oauth2/access_token'
    resp = request.get(openIdUrl, params=param)
    # {openid, accss_token, refresh_token, openid, scope, expires_in}
    # openId = json.loads(resp.text)['openid']
    return resp.text
#3.微信统一下,单统一下单时参数传递需要签名(微信用我们设定的密匙对参数进行MD5加密, 通过双方的签名判断请求是否被篡改)签名算法
@classmethod
def getSign(signkey, kwargs):
    # 计算签名
    keys, paras = sorted(kwargs), []
    paras = ['{}={}'.format(key, kwargs[key]) for key in keys if key != 'appkey']  # and kwargs[key] != '']
    stringA = '&'.join(paras)
    stringSignTemp = stringA + '&key=' + signkey
    sign = MD5(stringSignTemp).upper()
    return sign
# 获取MD5
def MD5(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()
#参数转xml
@classmethod
def getxml(signkey,kwargs):
    kwargs['sign'] = getSign(signkey,kwargs)
    # 生成xml
    xml = ''
    for key, value in kwargs.items():
        xml += '<{0}>{1}</{0}>'.format(key, value)
    xml = '<xml>{0}</xml>'.format(xml)
    # print(xml)
    return xml
#统一下单
def order(ordertotal,code,appid,secret,ordercode,noncestr,mchid,tradetype,signkey):
    startime=time.strptime(datetime.datetime.now(), "%Y%m%d%H%M%S")
    endtime=time.strptime(datetime.datetime.now()+datetime.timedelta(days=1), "%Y%m%d%H%M%S")
    UnifieOrderRequest = {
        'appid':appid,  # 公众账号ID
        'body': '测试-商品',  # 商品描述
        'mch_id': mchid,  # 商户号:深圳市泽慧文化传播有限公司
        'nonce_str': noncestr,  # 随机字符串
        'notify_url': 'https://service.huizeguoxue.com/service/applesson/wechatordernotice',  # 微信支付结果异步通知地址
       # 'openid': '',  # trade_type为JSAPI时，openid为必填参数！此参数为微信用户在商户对应appid下的唯一标识, 统一支付接口中，缺少必填参数openid！
        'trade_type': tradetype,  # 交易类型
        'time_start':startime,#交易开始时间
        'time_expire':endtime#交易结束时间
    }
    UnifieOrderRequest['nonce_str'] = str(uuid.uuid1()).replace("-","")
    if tradetype=="JSAPI":
        openidresp = getOpenID({'code': code, 'appid': appid, 'secret': secret})
        openid = json.loads(openidresp).get('openid')
        UnifieOrderRequest['openid'] = openid
    UnifieOrderRequest['out_trade_no'] = ordercode  # 内部订单号码
    UnifieOrderRequest['spbill_create_ip'] = "182.92.0.143"#终端ip
    UnifieOrderRequest['total_fee'] = int(0.01 * 100)
    # 签名并生成xml
    xml = getxml(signkey,UnifieOrderRequest)
    resp = request.post("https://api.mch.weixin.qq.com/pay/unifiedorder", data=xml.encode('utf-8'),
                         headers={'Content-Type': 'text/xml'})
    msg = resp.text.encode('ISO-8859-1').decode('utf-8')
    xmlresp = xmltodict.parse(msg)
    result = {}
    if xmlresp['xml']['return_code'] == 'SUCCESS':
        if xmlresp['xml']['result_code'] == 'SUCCESS':
            prepay_id = xmlresp['xml']['prepay_id']
            #操作数据库
            ordertotal.prepayid=prepay_id
            ordertotal.paytype="1"
            ordertotal.save()
            timestamp = str(int(time.time()))
            if tradetype=="JSAPI":
                para = {}
                para["appId"] = xmlresp['xml']['appid']
                para["nonceStr"] = noncestr
                prepayid = xmlresp['xml']['prepay_id']
                para["timeStamp"] = str(int(time.time()))
                para["package"] = "prepay_id="+prepayid
                para["signType"]="MD5"
                para["paySign"] = getSign(signkey, para)
                para["packageValue"] ="prepay_id="+prepayid
                result["para"] = json.dumps(para)
                result["mag"] = "成功"
                result["paystate"] = 1
                return result
            else:
                para = {}
                para["appid"] = xmlresp['xml']['appid']
                para["noncestr"] = noncestr
                mchid = xmlresp['xml']['mch_id']
                if mchid is not None:
                    para["partnerid"] = mchid
                para["prepayid"] = xmlresp['xml']['prepay_id']
                para["timestamp"] = str(int(time.time()))
                para["package"] = "Sign=WXPay"
                para["sign"] = getSign(signkey, para)
                para["packageValue"] = "Sign=WXPay"
                result["para"] = json.dumps(para)
                result["mag"] = "成功"
                result["paystate"] = 1
                # 签名后返回给前端做支付参数
                return result
        else:
            msg = xmlresp['xml']['err_code_des']
            result["mag"]=msg
            result["paystate"] = 0
            return result
    else:
        msg = xmlresp['xml']['return_msg']
        result["mag"] = msg
        result["paystate"] = 0
        return result
#查询微信订单
def query(ordercode,appid,mchid,noncestr,signkey):
    # 查询微信付款情况
    orderquery = {
        'appid': appid,#公众账号ID
        'mch_id': mchid,#商户号
        'nonce_str': noncestr,#随机字符串
        'out_trade_no': ordercode#商户订单号
    }
    xml = getxml(signkey,orderquery)
    resp = request.post("https://api.mch.weixin.qq.com/pay/orderquery", data=xml.encode('utf-8'),
                         headers={'Content-Type': 'text/xml'})
    msg = resp.text.encode('ISO-8859-1').decode('utf-8')
    xmlresp = xmltodict.parse(msg)
    result={"paystate":0}
    if xmlresp['xml']['return_code'] == 'SUCCESS':
        if xmlresp['xml']['result_code'] == 'SUCCESS':
            if xmlresp['xml']['trade_state'] == 'SUCCESS':
               # msg = xmlresp['xml']['trade_state_desc']#已经支付
                result["msg"]="已经支付"
                return result
            elif xmlresp['xml']['trade_state'] == 'CLOSED':
                #msg = xmlresp['xml']['trade_state_desc']
                result["msg"] = "订单已关闭，请重新下单！"
                return result
            elif xmlresp['xml']['trade_state'] == 'REFUND':
                #msg = xmlresp['xml']['trade_state_desc']
                result["msg"] = "转入退款！"
                return result
            elif xmlresp['xml']['trade_state'] == 'USERPAYING':
                #msg = xmlresp['xml']['trade_state_desc']
                result["msg"] = "用户支付中！"
                return result
            else:
                result["msg"] = xmlresp['xml']['trade_state_desc']
                para={}
                para["appid"]=xmlresp['xml']['appid']
                para["noncestr"] =noncestr
                mchid= xmlresp['xml']['mch_id']
                if mchid is not None:
                    para["partnerid"] =mchid
                para["prepayid"] = xmlresp['xml']['prepay_id']
                para["timestamp"] =str(int(time.time()))
                para["package"] = "Sign=WXPay"
                para["sign"] = getSign(signkey,para)
                para["packageValue"] = "Sign=WXPay"
                result["para"]=json.dumps(para)
                result["paystate"] = 1
                return result
        else:
            result["msg"] = xmlresp['xml']['err_code_des']
            result["paystate"] = 2
            return result
    else:
        result["msg"] = xmlresp['xml']['return_msg']
        result["paystate"] = 2
        return result
#app微信支付(注释：小程序下单只能用小程序支付)
def wxapppay(ordertotal):
    time1=ordertotal.ordertime+datetime.timedelta(hours=2)#添加2小时后的时间
    appid = settings.MyFishAppPayAppid
    mchid = settings.MyFishAppPayMchid
    noncestr = str(uuid.uuid1()).replace("-", "")
    signkey = settings.MyFishAppPaySignKey
    if ordertotal.prepayid is not None and ordertotal.prepayid!="" and time1>=datetime.datetime.now():
        return query(ordertotal.ordercode,appid,mchid,noncestr,signkey)
    else:
        return order(ordertotal, "", appid, "", ordertotal.ordercode, noncestr, mchid, "APP", signkey)
#js微信支付(code 和secret 是为了获取openid,这个应该在微信登录存入数据库，然后从数据库获得)
def wxjsapipay(ordertotal,code):
    appid = settings.MyFishJsPayAppid
    mchid = settings.MyFishJsPayMchid
    noncestr = str(uuid.uuid1()).replace("-", "")
    signkey = settings.MyFishJsPaySignKey
    secret=settings.MyFishJsPayAppSecret
    return order(ordertotal, code, appid, secret, ordertotal.ordercode, noncestr, mchid, "JSAPI", signkey)
#微信小程序(code 和secret 是为了获取openid,这个应该在微信登录存入数据库，然后从数据库获得)
def wxsmallpay(ordertotal,code):
    appid = settings.MyFishWxAppid
    mchid = settings.MyFishAppPayMchid
    noncestr = str(uuid.uuid1()).replace("-", "")
    signkey = settings.MyFishAppPaySignKey
    secret = settings.MyFishWxSecret
    return order(ordertotal, code, appid, secret, ordertotal.ordercode, noncestr, mchid, "JSAPI", signkey)


