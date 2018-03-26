#! /usr/bin/env python2
# encoding=utf-8
import time, random, hashlib, json, urllib, sys, os

import requests

# 苹果的测试环境0,生产环境 v2
apns_production = 1
# 苹果的测试环境0,生产环境 v3
apns_production_boolean = True

''''' 
    极光key配置 
'''
apps = {
    'test': {
        "app_key": u'app_key',
        "master_secret": u'master_secret'
    },
    'product': {
        "app_key": u'app_key',
        "master_secret": u'master_secret'
    }
}

''''' 
    https request jpush v3 
'''


def https_request(app_key, body, url, content_type=None, version=None, params=None):
    https = requests.Session()
    https.auth = (app_key['app_key'], app_key['master_secret'])
    headers = {}
    headers['user-agent'] = 'jpush-api-python-client'
    headers['connection'] = 'keep-alive'
    headers['content-type'] = 'application/json;charset:utf-8'
    # print url,body
    response = https.request('POST', url, data=body, params=params, headers=headers)
    # 合并返回
    return dict(json.loads(response.content), **{'status_code': response.status_code})


''''' 
    jpush v3 params  
    支持离线消息，在线通知同时发送 
'''


def push_params_v3(content, receiver_value=None, n_extras=None, platform="ios,android"):
    global apns_production_boolean
    sendno = int(time.time() + random.randint(10000000, 99999900))
    payload = dict()
    payload['platform'] = platform

    payload['audience'] = {
        "alias": receiver_value
    }
    # 离线消息
    payload['message'] = {
        "msg_content": content,
        "extras": n_extras
    }
    # 在线通知
    payload['notification'] = {
        "android": {"alert": content, "extras": n_extras},
        "ios": {"alert": content, "sound": "default", "extras": n_extras},  # "badge":1,
    }
    payload['options'] = {"apns_production": apns_production_boolean, "time_to_live": 86400 * 3, 'sendno': sendno}

    return payload


''''' 
    jpush v3 request 
'''


def jpush_v3(app_key, payload):
    body = json.dumps(payload)
    # print body
    return https_request(app_key, body, "https://api.jpush.cn/v3/push", 'application/json', version=1)


''''' 
    http post 简单版,jpush v2 
'''


def jpush(push_params):
    url = 'http://api.jpush.cn:8800/sendmsg/v2/sendmsg'
    content = ""
    if push_params:
        para_data = urllib.urlencode(push_params)
        f = urllib2.urlopen(url, para_data)
        content = f.read()
    return content


''''' 
    jpush v2 
    #拼推送参数 
    @param int $sendno 发送编号。由开发者自己维护，标识一次发送请求 
    @param int $receiver_type 接收者类型。 
    1、指定的 IMEI。此时必须指定 appKeys。 
    2、指定的 tag。 
    3、指定的 alias。 
    4、 对指定 appkey 的所有用户推送消息。 
    @param string $receiver_value 发送范围值，与 receiver_type相对应。  
        1、IMEI只支持一个  
        2、tag 支持多个，使用 "," 间隔。 
        3、alias 支持多个，使用 "," 间隔。  
        4、不需要填 
    @param int apns_production: 1 生产，0 测试  
    @param int $msg_type 发送消息的类型：1、通知 2、自定义消息 
    @param string $msg_content 发送消息的内容。 与 msg_type 相对应的值 
    @param string $platform 目标用户终端手机的平台类型，如： android, ios 多个请使用逗号分隔 
'''


def push_params(keycfg, content, match_id=None, receiver_value=None, n_extras=None, receiver_type='3',
                platform="ios,android"):
    global apns_production
    msg = {"n_title": "APP名字", "n_content": content, "n_extras": n_extras}
    msg_content = json.dumps(msg)
    sendno = str(int(time.time() + random.randint(10000000, 99999900)))
    verification_code = hashlib.new("md5",
                                    sendno + receiver_type + receiver_value + keycfg['master_secret']).hexdigest()

    param = dict()
    param['sendno'] = sendno
    param['app_key'] = keycfg['app_key']
    param['receiver_type'] = receiver_type
    param['receiver_value'] = receiver_value
    param['verification_code'] = verification_code
    param['msg_type'] = '1'
    param['msg_content'] = msg_content
    param['platform'] = platform
    param['apns_production'] = apns_production
    param['time_to_live'] = str(3 * 86400)

    return param