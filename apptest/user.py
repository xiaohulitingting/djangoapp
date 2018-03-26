import json
from django.http import HttpResponse
from apptest.models import tmember
import time
import random
import uuid
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from apptest import log
from apptest import request as requestclass
from apptest.common import md5
from apptest import mymemcache
'''
从post中取得数据，如果不存在则默认值为1 
pageNumber = request.POST.get('pageNumber',1) 
从get中取得数据，如果不存在则默认值为1 
pageNumber = request.GET.get('pageNumber',1) 
从所有请求中取得数据，如果不存在则默认值为1 
pageNumber = request.REQUEST.get('pageNumber',1)
#增加 
models.UserInfo.objects.create(user='yangmv',pwd='123456')
或者
obj = models.UserInfo(user='yangmv',pwd='123456')
obj.save()
或者
dic = {'user':'yangmv','pwd':'123456'}
models.UserInfo.objects.create(**dic)
#快捷键
https://www.cnblogs.com/luolizhi/p/5610123.html
'''
c1=log.LOG('user')
memcache = mymemcache.MemcachedClient()
#注册
@csrf_exempt
def register(request):
    #jsondata=json.loads(request.body)
    time.sleep(0.1)#休眠100毫秒
    try:
        if request.method=="POST":
            telephone=request.POST.get('telephone')
            user=  tmember.objects.filter(telephone=telephone).count()
            if user>0:
                response_data = {"state": 0, "message": "该账号已存在","tele":telephone}
            else:
                timedate=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                nickname="yanwoo"+str(random.randint(100000, 1000000))
                password = request.POST.get('password')
                phoneid=request.POST.get('phoneID')
                version=request.POST.get('version')
                clienttype=request.POST.get('clienttype')
                code=uuid.uuid1()#相当于c#中的guid
                tmember.objects.create(createtime=timedate,appchannelinfoid=5,password=password,
                                       phoneid=phoneid,state="0",code=code,telephone=telephone,credits=0,level=0,version=version,
                                       clientostype=clienttype,nickname=nickname)
                response_data = {"state": 1, "message": "注册成功"}
        else:
            response_data={"state":0,"message":"请求失败"}

    except:
        c1.error()  # 使用系统自己的错误描述
        response_data = {"state": 0, "message": "内部服务器错误"}
    return HttpResponse(json.dumps(response_data, ensure_ascii=False))

#登录
@csrf_exempt
def login(request):
    try:
        if(request.method=="POST"):
            telephone=request.POST.get("telephone")
            userlist=tmember.objects.filter(telephone=telephone)[0]
            if(userlist.count()>0):
                user=userlist[0]
                password=request.POST.get("password")
                if(password==user.password.rstrip()):
                    version=request.POST.get("version")
                    money=0
                    if(user.logintime==None):#第一次登录
                        money=1
                    if(user.version!=version):
                        user.version=version
                    datatime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    user.logintime=datatime
                    user.save()#保存数据库
                    dict={"id":user.id,"birthday":"","credits":int(user.credits),"telephone":user.telephone,"nickname":user.nickname,"code":user.code}
                    response_data = {"state": 1, "message": "登录成功","data":dict,"money":money}
                else:
                    response_data = {"state": 0, "message": "密码错误"}
            else:
                response_data = {"state": 0, "message": "账号不存在"}
        else:
            response_data = {"state": 0, "message": "请求方式错误"}
    except:
        c1.error()
        response_data = {"state": 0, "message": "内部服务器错误"}
    return HttpResponse(json.dumps(response_data, ensure_ascii=False))
#修改密码
@csrf_exempt
def updatepassword(request):
    response_data={}
    response_data["state"] = 0
    try:
        if request.method=="POST":
            tele=request.POST.get("telephone")
            password=request.POST.get("password")
            newpass=request.POST.get("newpassword")
            userlist=tmember.objects.filter(telephone=tele)
            if userlist.count()>0:
                user=userlist[0]
                if user.password.rstrip()==password:
                    if newpass!="" and newpass!=None:
                        user.password=newpass
                        user.save()
                        response_data["message"] = "修改成功"
                        response_data["state"] = 1
            else:
                response_data["message"] = "账户不存在"
        else:
            response_data["message"]="请求方式错误"
    except:
       c1.error()
       response_data["message"] = "内部服务器错误"
    return HttpResponse(json.dumps(response_data,ensure_ascii=False))
#获取用户信息
@csrf_exempt
def getuserinfo(request):
    response_data={}
    response_data["state"]=0
    try:
        if request.method=="POST":
            tele=request.POST.get("telephone")
            userlist=  tmember.objects.filter(telephone=tele)
            if userlist.count()>0:
                user=userlist[0]
                data={}
                data["telephone"]=user.telephone
                data["nickname"]=user.nickname
                data["headpath"]=user.headpath
                data["id"]=user.id
                data["code"]=user.code
                data["sex"]=user.sex
                response_data["data"]=data
                response_data["message"] = "获取成功"
                response_data["state"] = 1
            else:
                response_data["message"] = "用户不存在"
        else:
            response_data["message"] = "请求方式错误"
    except:
        c1.error()
        response_data["message"]="内部服务器错误"
    return HttpResponse(json.dumps(response_data,ensure_ascii=False))
#发送验证码
#创建者：hlt
#创建时间：2018-03-13
@csrf_exempt
def getmessagecode(request):
    response_data = {}
    response_data["state"] = 0
    try:
        if request.method == "POST":
            tele = request.POST.get("telephone")
            use="zyyd"#短信用户名
            num = str(random.randint(100000, 1000000)) # 验证码
            pwd=md5("Zy1130813")#加密后的密码
            content = "[燕喔喔]：您的验证码是：" + num + "请及时输入。如非本人操作请忽略此短信"
            content=content.encode("utf-8")
            values={"u":use,"p":pwd,"m":tele,"c":content}
            result= requestclass.get("http://api.smsbao.com/sms",values)
            if result=='0':
                val=memcache.get(tele)
                if val!=None:
                    memcache.delete(tele)
                memcache.set_timeout(tele,num,60)#60秒失效
                response_data["message"] = "获取成功"
                response_data["state"] = 1
                response_data["data"] = num
        else:
            response_data["message"] = "请求方式错误"
    except:
        c1.error()
        response_data["message"] = "内部服务器错误"
    return HttpResponse(json.dumps(response_data, ensure_ascii=False))
#校验验证码
#创建者：hlt
#创建时间：2018-03-13
@csrf_exempt
def checkmessagecode(request):
    response_data = {}
    response_data["state"] = 0
    try:
        if request.method == "POST":
            tele = request.POST.get("telephone")
            num = request.POST.get("number")
            if tele!=None and tele!="":
                val = memcache.get(tele)
                result = ""
                if val != None:
                    result = str(val, "utf-8")
                    if result == num:
                        response_data["message"] = "校验成功"
                        response_data["state"] = 1
                else:
                    response_data["message"] = "验证码失效"
            else:
                response_data["message"] = "手机号不能为空"

        else:
            response_data["message"] = "请求方式错误"
    except:
        c1.error()
        response_data["message"] = "内部服务器错误"
    return HttpResponse(json.dumps(response_data, ensure_ascii=False))
#测试memcache缓存
#创建者：hlt
#创建时间：2018-03-13
@csrf_exempt
def getmemcache(request):
    response_data = {}
    response_data["state"] = 0
    try:
        if request.method == "POST":
            #memcache.set_timeout("name", "xiaohuli",60)
            val= memcache.get("name")
            result=""
            if val!=None:
                result = str(val, "utf-8")
            response_data["message"] = "data is xiaohuli"
            response_data["state"] = 1
            response_data["data"] = result
        else:
            response_data["message"] = "请求方式错误"
    except:
        c1.error()
        response_data["message"] = "内部服务器错误"
    return HttpResponse(json.dumps(response_data, ensure_ascii=False))



