from django.shortcuts import render
#from apptest.models import Dreamreal
from django.http import HttpResponse
from django.core import serializers
import json
# Create your views here.
'''
def home(request):
    title="欢迎学习django"
    list=[1,2,3]
    return render(request, 'home.html', {'title': title,'list':list})
def adddb(request):
    dreamreal = Dreamreal( website = "www.polo.com", mail = "sorex@polo.com",
      name = "sorex", phonenumber = "002376970")
    dreamreal.save()
    
     
     response_data = {}
    response_data['result'] = 'success'
    response_data['message'] = '数据添加成功'
    
   
    
    response_data = {'errorcode': 100, 'detail': '数据添加成功'}
    #return HttpResponse("<p>数据添加成功！</p>")
    return HttpResponse((response_data), content_type="application/json;charset=utf-8")
#获取数据
def selectdb(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Dreamreal.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Dreamreal.objects.filter(id=1)
    # 获取单个对象
    response3 = Dreamreal.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Dreamreal.objects.order_by('name')[0:2]

    # 数据排序
    Dreamreal.objects.order_by("id")

    # 上面的方法可以连锁使用
    Dreamreal.objects.filter(name="sorex").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += str(var.id) + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")


# 更新数据
def updatedb(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Dreamreal.objects.get(id=1)
    test1.name = 'Google'
    test1.save()

    # 另外一种方式
    # Test.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")


# 删除数据
def deletedb(request):
    # 删除id=1的数据
    test1 = Dreamreal.objects.get(id=1)
    test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()
    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")
def search(request):
    #http://blog.51cto.com/rmeos/1765183  多条件查询
    
    ctx = {}
        if request.POST:
        ctx['rlt'] = request.POST['q']


            response2 = Dreamreal.objects.filter(id=1)
    response2 = Dreamreal.objects.filter(id=1)

    
    #id=request.GET["id"];
   # response = Dreamreal.objects.filter(id=id)
    #data = serializers.serialize("json", response,ensure_ascii = False)
    return HttpResponse(data)
'''