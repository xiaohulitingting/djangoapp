from django.shortcuts import render
from django.http import HttpResponse
from apptest.form import LoginForm
import json


def login(request):
    return render(request,"login.html")
def loginForm(request):
    response_data={}
    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():
            user = f.cleaned_data["username"]
            pwd = f.cleaned_data["password"]
            if(user=="admin" and pwd=="123456"):
                response_data["State"] =0
                response_data["message"] ='登录成功'
            else:
                response_data["State"] = 1
                response_data["message"] = "密码错误"
        else:
            response_data["State"] = 1
            response_data["message"] = f.errors
    else:
        response_data = {'State': 1, 'message': '登录失败'}
    return HttpResponse(json.dumps(response_data,ensure_ascii=False))