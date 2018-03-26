from apptest import log,common,models,sqlexecute
import json,time,datetime,uuid,random
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from myprojecttest import settings
from django.db import transaction
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
                    firstpageProductManager=sqlexecute.FirstpageProductManager(str(productid))
                    dict=firstpageProductManager.with_counts()
                    if dict.__len__()>0:
                         firstpageproductodel["producttypeid"]=dict["id"]
                         firstpageproductodel["producttypename"] = dict["name"]
            return_list.append(firstpageproductodel)
            i = i + 1
    return return_list
##获取分类id获取商品
#创建者：hlt
#创建时间：2018-03-15
@csrf_exempt
def getproductlistbytypeid(request):
    response_data={'state':0}
    try:
        if request.method=="POST":
            typeid=int(request.POST.get("producttypeid",0))
            pageindex=int(request.POST.get("pageindex",1))
            pagesize = int(request.POST.get("pagesize", 10))
            getProductByTypeidManager= sqlexecute.GetProductByTypeidManager(typeid,pagesize*(pageindex-1),pagesize)
            tuple=getProductByTypeidManager.queryProduct()
            resproductlist=[]
            for row in tuple:
                resproductmodel={"price":row[9],"productid":row[0],"productname":row[4],"status":row[28]}
                imglist = models.TProductImages.objects.filter(fk_productid=row[0],ismain="1").order_by("sort")
                if imglist.count()>0:
                    resproductmodel["imgpath"]=getimglistpath(imglist[0].path)
                else:
                    resproductmodel["imgpath"] = ""
                resproductlist.append(resproductmodel)
            response_data["message"] = "请求成功"
            response_data["state"] = 1
            response_data["data"] = resproductlist
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
##商品详情
#创建者：hlt
#创建时间：2018-03-14
@csrf_exempt
def productdetail(request):
    response_data={"state":0}
    try:
       if request.method=="POST":
           pid=int(request.POST.get("productid","0"))#商品id
           userid=int(request.POST.get("userid","0"))#用户id
           productlist= models.TProduct.objects.filter(id=pid)
           if productlist.count()>0:
               model=productlist[0]
               resproductmodel = {}
               resproductmodel["price"]=str(model.currentsaleprice)
               resproductmodel["productid"]=model.id
               resproductmodel["productname"] = model.productname
               resproductmodel["status"] = model.status
               resproductmodel["supplierid"] = model.fk_supplierid
               resproductmodel["suppliername"] = getsuppliername(model.fk_supplierid)
               if model.service is not None and model.service!="":
                   resproductmodel["service"] = model.service.replace("</br>", "\r\n")
               else:
                   resproductmodel["service"] = model.service
               resproductmodel["detailurl"] = model.graphicdetailspath+ "?standard="+ settings.GraphicDetailsPath
               resproductmodel["remark"] = model.remark
               if userid>0:
                   dict= iscollection(model.id,userid)
                   resproductmodel["collectionstate"] = dict["collectionstate"];  # 未收藏
                   resproductmodel["collectionid"] = dict["collectionid"]
               else:
                   resproductmodel["collectionstate"] ="0"; # 未收藏
                   resproductmodel["collectionid"] = "0"
               resproductmodel["tags"]=gettags(model.tagids)
               resproductmodel["img"] =getproductimg(model.id)#获取商品图片
               resproductmodel["attributegroup"] =getattribute(model.id)#获取属性集合
               resproductmodel["discountinfo"] = getproductdiscount(model.id,userid)  #获取属性集合
               flag= addbrowse(userid,model.id,model.fk_supplierid)
               response_data["message"] = "请求成功"
               response_data["state"] = 1
               if flag:
                   response_data["data"] = resproductmodel

           else:
               response_data["message"] = "商品不存在"
       else:
           response_data["message"] = "请求方式错误"
    except:
        c1.error()
        response_data["message"]="内部服务器错误"
    return HttpResponse(json.dumps(response_data,ensure_ascii=False))
#获取商品sku
#创建者：hlt
#创建时间：2018-03-15
@csrf_exempt
def getsku(request):
    response_data={"state":0}
    try:
        if request.method=="POST":
           # ss=request.session.get("test3",None)
            #request.session["test2"]='hhh'
            productid=int(request.POST.get("productid",0))
            getskulist=models.TProductSku.objects.filter(fk_productid=productid)
            reslist=[]
            skuAttributionList=[]
            skuList=[]
            skuvaluelist=[]
            if getskulist.count()>0:
                #跟商品有关的sku属性
                code=1001
                for item in getskulist:
                    attributename = models.TAttribute.objects.get(id=item.fk_attributeid).attributename
                    skuAttributionModel={"attributeid":item.fk_attributeid,"attributename":attributename}
                    skuAttributionValueList=[]
                    skuAttributionValue=[]
                    klist=models.TProductSku.objects.filter(skucode=item.skucode,fk_attributeid=item.fk_attributeid)
                    for kitem in klist:
                        if kitem.attributevalue not in skuAttributionValue:
                            skuAttributionValuemodel={"AttributeID":kitem.fk_attributeid,"AttributeValue":kitem.attributevalue,"AttributeValueID":code}
                            code=code+1
                            skuAttributionValueList.append(skuAttributionValuemodel)
                            skuAttributionValue.append(kitem.attributevalue)
                    skuAttributionModel["AttributeValues"]=skuAttributionValueList
                    skuAttributionList.append(skuAttributionModel)
                #sku
                allsku=models.TProductSku.objects.filter(skucode=getskulist[0].skucode)
                for skuitem in allsku:
                    if skuitem.fk_productid not in skuvaluelist:
                        product=models.TProduct.objects.get(id=skuitem.fk_productid)
                        skumodel = {"id": skuitem.fk_productid, "productname": product.productname,
                                    "price": product.currentsaleprice, }
                        imglist = models.TProductImages.objects.filter(fk_productid=product.id, ismain=1)
                        if (imglist.count() > 0):
                            skumodel["img"] = getimglistpath(imglist[0].path)
                        else:
                            skumodel["img"] = ""
                        skuAttributionValueList=[]
                        for skuAttributionitem in skuAttributionList:
                            if skuAttributionitem["attributeid"] == skuitem.fk_attributeid:
                                AttributeValuesList = skuAttributionitem["AttributeValues"]
                                for AttributeValuesitem in AttributeValuesList:
                                    if AttributeValuesitem["AttributeValue"] == skuitem.attributevalue:
                                        SKUAttributionValueModel={"AttributeID":skuitem.fk_attributeid,"AttributeValue":skuitem.attributevalue,"AttributeValueID":AttributeValuesitem["AttributeValueID"]}
                                        skuAttributionValueList.append(SKUAttributionValueModel)
                                        skumodel["AttributeValueIDs"]=AttributeValuesitem["AttributeValueID"]
                                        break
                        skumodel["Attributes"]=skuAttributionValueList
                        skuList.append(skumodel)
                        skuvaluelist.append(skuitem.fk_productid)
                    else:
                        for skuAttributionitem1 in skuAttributionList:
                            if skuAttributionitem1["attributeid"] == skuitem.fk_attributeid:
                                AttributeValuesList1 = skuAttributionitem1["AttributeValues"]
                                for AttributeValuesitem1 in AttributeValuesList1:
                                    if AttributeValuesitem1["AttributeValue"] == skuitem.attributevalue:
                                        SKUAttributionValueModel1={"AttributeID":skuitem.fk_attributeid,"AttributeValue":skuitem.attributevalue,"AttributeValueID":AttributeValuesitem1["AttributeValueID"]}
                                        for ii in skuList:
                                            if skuitem.fk_productid==ii["id"]:
                                                lastlist=ii["Attributes"]
                                                lastlist.append(SKUAttributionValueModel1)
                                                ii["AttributeValueIDs"]=str(ii["AttributeValueIDs"])+','+str(AttributeValuesitem1["AttributeValueID"])
                                                break

            reslist.append(skuAttributionList)
            reslist.append(skuList)
            response_data["message"] = "请求成功"
            response_data["state"] = 1
            response_data["data"] = reslist

        else:
            response_data["message"]="内部服务器错误"
    except:
        c1.error()
        response_data["message"]="内部服务器错误"
    return HttpResponse(json.dumps(response_data,ensure_ascii=False))
#根据商品id获取商品一级分类
#创建者：hlt
#创建时间：2018-03-15
@csrf_exempt
def getproducttypebyid(request):
    response_data={"state":0}
    try:
        if request.method=="POST":
            #request.session["test3"] = "testvalue"
            #request.session.set_expiry(60)
           #  request.session.set_expiry(60)
            #sess= request.session.get("test2",None)
           #  request.session["test1"] = "testvalue1"
            #sess1 = request.session.get("test1",None)
            productid=int(request.POST.get("productid",0))
            productlist=models.TProduct.objects.filter(id=productid).only("fk_producttypebrandid")
            if productlist.count()>0:
                product=productlist[0]
                producttypebrand= models.TProductTypebrand.objects.filter(id=product.fk_producttypebrandid).only("fk_producttypeid")
                producttypelist=models.TProductType.objects.filter().values("id","fatherid","name","grade")
                id=producttypebrand[0].fk_producttypeid
                response_data["data"]=getlastproducttype(id,producttypelist)
                response_data["message"]="获取成功"
                response_data["state"]=1
            else:
                response_data["message"]="商品不存在"
        else:
            response_data["message"]="请求方式错误"
    except:
        c1.error()
        response_data["message"]="内部服务器错误"
    return HttpResponse(json.dumps(response_data,ensure_ascii=False))
def getlastproducttype(producttypeid,producttypelist):
    mm=producttypelist.get(id=producttypeid)
    if mm["grade"]==1:
       return {"typeid": mm["id"], "typename": mm["name"]}
    else:
       return getlastproducttype(mm["fatherid"],producttypelist)
#根据商品一级分类获取商品
#创建者hlt
#创建时间：2018-03-16
@csrf_exempt
def getproductbytype1(request):
    response_data = {"state": 0}
    try:
        if request.method == "POST":
            producttypeid = int(request.POST.get("producttypeid", 0))
            typelist=models.TProductType.objects.all().values("id","fatherid","ischildren")
            typeidlist=[]
            typeid=   gettypeidnochildren(typelist,producttypeid,typeidlist)
            para=tuple(typeid)
            resulttuple=models.TProductTypebrand.objects.extra(where=['fk_producttypeid IN %s'],params=[para]).values_list("id", flat=True)
            productlist=models.TProduct.objects.filter(status='3').extra(where=['fk_producttypebrandid In %s'],params=[tuple(resulttuple)]).values("id","productname","status","currentsaleprice").order_by("-salenumber")[0:10]
            resultlist = []
            for item in productlist:
                productmodel = {}
                productmodel["price"] = item["currentsaleprice"]
                productmodel["productid"] = item["id"]
                productmodel["productname"] = item["productname"]
                productmodel["status"] = item["status"]
                imglist = models.TProductImages.objects.filter(fk_productid=item["id"], ismain=1)
                if (imglist.count() > 0):
                    productmodel["img"] = imglist[0].path
                else:
                    productmodel["img"] = ""
                resultlist.append(productmodel)
            response_data["message"] = "获取成功"
            response_data["state"] = 1
            response_data["data"] = resultlist
        else:
            response_data["message"] = "请求方式错误"
    except:
        c1.error()
        response_data["message"] = "内部服务器错误"
    return HttpResponse(json.dumps(response_data, ensure_ascii=False))
def gettypeidnochildren(typelist,producttypeid,typeidlist):
    mmlist=typelist.filter(fatherid=producttypeid)
    for item in mmlist:
        if item["ischildren"]=="0":
            typeidlist.append(item["id"])
        else:
            gettypeidnochildren(typelist, item["id"], typeidlist)
    return typeidlist
#获取供应商名称
def getsuppliername(supplierid):
    return models.TSupplier.objects.get(id=supplierid).suppliername
#是否收藏
def iscollection(productid,userid):
   list= models.TMemberCollection.objects.filter(fk_memberid=userid,fk_productid=productid,collectionstatus="1")
   dict={"collectionstate":"0","collectionid":"0"}
   if list.count()>0:
       dict["collectionstate"]="1"
       dict["collectionid"]=str(list[0].id)
   return dict
#得到商品标签
def gettags(tagid):
    returnlist=[]
    if tagid is not None and tagid!="":
        tagarr=tagid.split(',')
        q = Q()
        for item in tagarr:
            if item!="":
               tag= int(item)
               q.add(Q(**{"id": tag}), Q.OR)
        q.add(Q(**{"sign": "1"}), Q.AND)
        list= models.TTag.objects.filter(q)
        for row in list:
            returnlist.append(row.tagname)
    return returnlist
#得到商品图片
def getproductimg(productid):
    imglist=models.TProductImages.objects.filter(fk_productid=productid).order_by("sort")
    img=""
    for row in imglist:
        path=row.path
        img=img+getimgmainpath(path)+","
    return img
#得到商品主图
def getimgmainpath(path):
    if path!="" and path is not None:
        newpath=path.replace("/Upfile",settings.MyThumbImagePath)
        lastindex=newpath.rfind(".")
        length=len(newpath)
        substr=newpath[lastindex:length]
        utf8str=newpath[0:lastindex]+"_"+settings.ProductMainImageWidth+substr
        return utf8str
    else:
        return ""
#得到商品列表图片
def getimglistpath(path):
    if path!="" and path is not None:
        newpath=path.replace("/Upfile",settings.MyThumbImagePath)
        lastindex=int(newpath.rfind("."))
        length=int(len(newpath))
        substr=newpath[lastindex:length]
        utf8str=newpath[0:lastindex]+"_"+settings.ProductListImageWidth+substr
        return utf8str
    else:
        return ""
#获取属性集合
def getattribute(productid):
    productAttributeManager=sqlexecute.ProductAttributeManager(str(productid))
    list= productAttributeManager.queryAttribute()
    groupnamelist=[]
    attributegrouplist=[]
    for row in list:
        if row["groupname"] not in groupnamelist:
            groupnamelist.append(row["groupname"])
    for groupnameitem in groupnamelist:
        attributedict={"groupname":groupnameitem}
        attributelist = []
        for rowitem in list:
            if groupnameitem==rowitem["groupname"]:
                attributelist.append({"key":rowitem["attributename"],"value":rowitem["othervalue"]})
        attributedict["attribute"]=attributelist
        attributegrouplist.append(attributedict)
    return attributegrouplist
#获取商品优惠券集合
def getproductdiscount(productid,userid):
    now = datetime.datetime.now()
    list= models.TDiscount.objects.filter(checkstatus=2,getstartdatetime__lte=now,getenddatetime__gte=now,sendmode=0).filter(~Q(type = '1'))
    #商品分类逻辑未写
    discountlist=[]
    for row in list:
        if row.isallproduct=="0":
            discountlist.append(getdiscountinfo(row,userid))
        elif row.fk_promotionsmoduleid is not None and int(row.fk_promotionsmoduleid)>0:
            prolist=models.TPromotionsModule.objects.filter(fk_promotionsid=row.fk_promotionsmoduleid)
            if prolist.count()>0:
               pronewlist= models.TPromotionsNews.objects.filter(fk_pmoduleid=prolist[0].fk_moduleid,promotionsproductid=productid)
               if pronewlist.count()>0:
                    discountlist.append(getdiscountinfo(row, userid))
        elif row.fk_promotionsid is not None and int(row.fk_promotionsid)>0:
            promolist=models.TPromotions.objects.filter(id=row.fk_promotionsid)
            for prorow in promolist:
                prolist=models.TPromotionsModule.objects.filter(fk_promotionsid=prorow.id)
                if prolist.count() > 0:
                    pronewlist = models.TPromotionsNews.objects.filter(promotionsproductid=productid,fk_pmoduleid=prolist[0].fk_moduleid)
                    if pronewlist.count() > 0:
                        discountlist.append(getdiscountinfo(row, userid))

    return discountlist
#获取优惠券
def getdiscountinfo(row,userid):
    discontmodel = {}
    if row.getmode == 0:  # 只能领一次
        walletlist = models.TMemberWallet.objects.filter(fk_member=userid, fk_discount=row.id)
    else:  # 每天领一次
        walletlist = models.TMemberWallet.objects.filter(fk_member=userid).filter(Q(state=1), Q(
            createtime__day=datetime.datetime.day))
    if walletlist.count() > 0:
        discontmodel["state"] = "1"  # 1已领取
    else:
        discontmodel["state"] = "2"  # wei领取
    discontmodel["discountname"] = row.discountname
    discontmodel["EndTime"] = str(row.DiscountEndDateTime)[0:10]
    discontmodel["id"] = row.id
    discontmodel["money"] = row.discountdecproce
    discontmodel["starttime"] = str(row.discountstartdatetime)[0, 10]
    discontmodel["summoney"] = row.discountsumprice
    return discontmodel
#添加浏览足迹
def addbrowse(userid,productid,supplierid):
    try:
        if userid > 0:
            blist = models.TMemberBrowse.objects.filter(fk_productid=productid, fk_memberid=userid)
            with transaction.atomic():
                if blist.count() == 0:
                    models.TMemberBrowse.objects.create(browernumber=1, fk_memberid=userid, fk_productid=productid,
                                                        fk_supplierid=supplierid,
                                                        lastbrowsedatetime=datetime.datetime.now(), remark="")

                    updateproduct(1, productid)
                    return True
                else:
                    bmodel = blist[0]
                    bmodel.lastbrowsedatetime = datetime.datetime.now()
                    bmodel.browernumber = bmodel.browernumber + 1
                    bmodel.save()
                    updateproduct(1, productid)
                    return True
        else:
            updateproduct(1, productid)
            return True
    except:
        return False
#更新商品数量
def updateproduct(type,productid):
    productlist=models.TProduct.objects.filter(id=productid)
    if productlist.count()>0:
        productmodel=productlist[0]
        if type==1:#浏览
            productmodel.browsenumber=productmodel.browsenumber+1
        else:#收藏
            productmodel.collectionnumber=productmodel.collectionnumber+1
        productmodel.save()
        return True
    else:
        return False
