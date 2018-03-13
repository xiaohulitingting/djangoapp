from apptest import log,common,models
import json,time,datetime,uuid,random
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#获取首页商品
#创建者：hlt
#创建时间：2018-03-13
c1=log.LOG("product")
@csrf_exempt
def getfirstpage(request):
    response_data={'state':0}
    try:
       if request.method=="POST":
           version=request.POST.get('fversion')
           if version==None or (version!=None and version.strip()==""):
               version="1.0.0"
           query={"state":1,"version":version}
           typeList=models.TFirstpageProducttype.objects.filter(**query)
           list=[]
           rlist=[]
           for type in typeList:
               if type.endtime is not None:
                   datetime1= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                   endtime=str(type.endtime)
                   if endtime>=datetime1:
                       typemodel={}
                       typemodel["typeid"]=str(type.id)
                       typemodel["typecode"] = str(type.typecode)
                       typemodel["modulename"] =type.typename
                       typemodel["sort"] = str(type.sort)
                       query1 = {"state": "1", "fk_type": type.id}
                       list=models.TFirstpageProduct.objects.filter(**query1)
                       typemodel["data"]=getfirstproduct(list,type.num,type.typecode)
                       rlist.append(typemodel)
               else:
                   typemodel = {}
                   typemodel["typeid"] = str(type.id)
                   typemodel["typecode"] = str(type.typecode)
                   typemodel["modulename"] = type.typename
                   typemodel["sort"] = str(type.sort)
                   query1 = {"state": "1", "FK_Type": type.id}
                   list = models.TFirstpageProduct.objects.filter(**query1)
                   typemodel["data"] = getfirstproduct(list, type.num, type.typecode)
                   rlist.append(typemodel)
           response_data["message"] = "请求成功"
           response_data["state"] = 1
           response_data["result"] = rlist
       else:
           response_data["message"] = "请求方式错误"
    except:
        c1.error()
        response_data["message"]="服务器内部异常"
    return HttpResponse(json.dumps(response_data, ensure_ascii=False))
def getfirstproduct(list,count,typecode):
    return_list=[]
    num=list.count()
    if num>=count:
        num=count
    i = 0
    for item in list:
        while (i < num):
            firstpageproductodel={}
            firstpageproductodel["desc"]=item.descs
            firstpageproductodel["imgurl"] = item.img
            firstpageproductodel["link"] = item.url
            firstpageproductodel["productsaleprice"] = str(item.product_saleprice)
            firstpageproductodel["title"] = item.head
            if item.fk_product is not None:
                firstpageproductodel["productid"] = str(item.fk_product)
                if typecode==1011:
                    productid=item.fk_product
                    firstpageProductManager=models.FirstpageProductManager(str(productid))
                    dict=firstpageProductManager.with_counts()
                    if dict.__len__()>0:
                         firstpageproductodel["producttypeid"]=dict["id"]
                         firstpageproductodel["producttypename"] = dict["name"]
            return_list.append(firstpageproductodel)
            i = i + 1
    return return_list
##获取分类id获取商品
#创建者：hlt
#创建时间：2018-03-13
@csrf_exempt
def getproductlistbytypeid(request):
    response_data={'state':0}
    try:
        if request.method=="POST":
            typeid=request.POST.get("producttypeid")
            pageindex=request.POST.get("pageindex",1)
            pageindex = request.POST.get("pagesize", 10)
        else:
            response_data["message"] = "请求方式错误"
    except:
        c1.error()
        response_data["message"]="内部服务器错误"
    return HttpResponse(json.dumps(response_data,ensure_ascii=False))
##搜索商品
#创建者：hlt
#创建时间：2018-03-13
@csrf_exempt
def searchproduct(request):
    response_data={'state':0}
    try:
        if request.method=="POST":
            tag=request.POST.get("tag")
            pageindex=int(request.POST.get("pageindex",1))
            pagesize = int(request.POST.get("pagesize", 10))
            start=(pageindex-1)*pagesize
            end=start+pagesize
            list= models.TProduct.objects.filter(status='3',productname__contains=tag)[start:end]
            resultlist=[]
            for item in list:
                productmodel={}
                productmodel["price"]=item.currentsaleprice
                productmodel["productid"] = item.id
                productmodel["productname"] = item.productname
                productmodel["status"] = item.status
                imglist= models.TProductImages.objects.filter(fk_productid=item.id, ismain=1)
                if(imglist.count()>0):
                   productmodel["img"] = imglist[0].path
                else:
                    productmodel["img"] = ""
                resultlist.append(productmodel)
            response_data["message"] = "请求成功"
            response_data["state"] = 1
            response_data["data"] = productmodel
        else:
            response_data["message"] = "请求方式错误"
    except:
        c1.error()
        response_data["message"]="内部服务器错误"
    return HttpResponse(json.dumps(response_data,ensure_ascii=False))

