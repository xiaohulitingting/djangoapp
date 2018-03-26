#coding:utf-8
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
#支付回调
#支付宝回调
from Crypto.PublicKey import RSA
import base64
import requests

# 支付宝 RSA 公钥
ALIPAY_RSA_PUBLIC_KEY_PATH = 'alipay_rsa_public_key.pem'

# 验证是否是支付宝发来的通知链接地址
ALIPAY_REMOTE_ORIGIN_URL = 'https://mapi.alipay.com/gateway.do'

@csrf_exempt
def paycallbackAliPay(request):
    if request.method == 'POST':
        if not len(request.POST) > 0:
            return HttpResponse(status=400)
        # �验证签名 sign
        if verifySignString(request.POST):
            notify_id = request.POST['notify_id']
            parter = request.POST['seller_id']
            # 验证是否是支付宝发来的通知
            if verifyURL(parter,notify_id):
                # 处理服务器端逻辑，更新数据库等
                # ...
                # ...
                # ...
                # 向支付宝返回�成功接收并处理异步通知状态
                return HttpResponse("SUCCESS")
    return HttpResponse(status=400)

# 验证签名
# params：request.POST
def verifySignString(self,params):
    if not len(params) > 0:
        return False
    key_sorted = sorted(params.keys())
    content = ''
    sign_type = params["sign_type"]
    signOrigin = params["sign"]

    for key in key_sorted:
        if key not in ["sign","sign_type"]:
            if len(params[key]) > 0:
                content = content + key + "=" + params[key] + "&"
    content = content[:-1]
    content = content.encode("utf-8")
    # print "content -> " + content

    if sign_type.upper() == "RSA":
        try:
            with open(ALIPAY_RSA_PUBLIC_KEY_PATH) as publickfile:
                pub = publickfile.read()
            pubkey = RSA.PublicKey.load_pkcs1_openssl_pem(pub)

            # �支付宝返回的 sign 经过 base64 encode，先 decode 一下
            signatureString = base64.decodestring(signOrigin)
            if RSA.verify(content, signatureString, pubkey):
                # print "----------verify sign success----------"
                return True
        except:
            # print "----------verify sign failed----------"
            return False
    else:
        # �支付宝当前仅支持 RSA 加密，未来也许会有其他类型
        return False

    return False

# 验证是否是支付宝发来的通知
# partner：request.POST["seller_id"]，也可以 hardcode
# notify_id：request.POST["notify_id"]
def verifyURL(self, partner, notify_id):
    payload = {'service':'notify_verify','partner':partner,'notify_id':notify_id}
    urlString = ALIPAY_REMOTE_ORIGIN_URL
    r = requests.get(urlString,params=payload)
    result = r.text
    # print result
    if result.upper() == "TRUE":
        # print "----------verify �url success----------"
        return True
    return False
