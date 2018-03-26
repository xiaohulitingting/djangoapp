# coding:utf-8
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from apptest import models ,sqlexecute,common,log as log
from django.db import transaction
from django.db.models import Q
import datetime,json,uuid
c1=log.LOG("order")
@csrf_exempt
def createorder(request):
    response_data={"state":0}
    try:
        if request.method=="POST":
            json_data = json.loads(request.body)
            sumprice=float(json_data["sumprice"])
            userid=json_data["userid"]
            addressid=json_data["addressid"]
            walletid=json_data["walletid"]
            orderproductList=json_data["orderproduct"]
            if sumprice>=0 and userid>0 and addressid>0:
                 user=models.tmember.objects.get(id=userid)
                 addr=models.TMemberContact.objects.filter(id=addressid)
                 if addr.count()>0:
                     orderproductid = []
                     for orderproduct in orderproductList:
                         if orderproduct["productnumber"] <= 0 or orderproduct["price"]:
                             response_data["message"] = "参数错误"
                             break
                         orderproductid.append(orderproduct["productid"])
                     productlist = models.TProduct.objects.extra(where=["id IN %s"], params=[orderproductid])
                     checkresult = {}
                     if walletid > 0:
                         wallet = models.TMemberWallet.objects.filter(id=walletid, state=1)  # 红包信息
                         if wallet.count() > 0:
                             discount = models.TDiscount.objects.filter(Q(getstartdatetime__gt=datetime.datetime.now()),
                                                                        Q(getenddatetime__lt=datetime.datetime.now()))
                             if discount.count() > 0:
                                 checkresult= checkprice(sumprice,orderproductList,productlist,discount[0])
                             else:
                                 response_data["message"] = "红包不可用"
                                 return HttpResponse(json.dumps(response_data, ensure_ascii=False))
                         else:
                             response_data["message"] = "红包不可用"
                             return HttpResponse(json.dumps(response_data, ensure_ascii=False))
                     else:
                         checkresult=checkprice(sumprice,orderproductList,productlist,None)
                     if checkresult["state"]==1:
                         ordercode=insertorder(wallet,addr,userid,checkresult["totalmoney"],discount,walletid,checkresult["buyprice"],checkresult["reqOrderSupplierdict"],checkresult["walletproduct"],checkresult["walletmoney"],productlist)
                         response_data["message"] = "下单成功"
                         response_data["state"] = 1
                         response_data["data"] = ordercode
                     else:
                         response_data["message"] = "下单失败"
                         return HttpResponse(json.dumps(response_data, ensure_ascii=False))
                 else:
                     response_data["message"] = "收获地址为空"
            else:
                response_data["message"] = "参数错误"
        else:
            response_data["message"]="请求方式错误"
    except:
        c1.error()
        response_data["message"]="内部服务器错误"
    return HttpResponse(json.dumps(response_data,ensure_ascii=False))
#校验下单价格
def checkprice(sumprice,orderproductlist,productlist,discount):
     totalmoney = 0
     buyprice=0
     walletmoney=0
     walletproduct=[]
     reqOrderSupplierdict={}
     supplierid=[]
     for orderproduct in orderproductlist:
        productmodel= productlist.get(id=orderproduct["productid"])
        if productmodel.status=="3" and productmodel.stocknumber>=orderproduct["productnumber"] and orderproduct["price"]==productmodel.currentsaleprice :
            totalmoney=totalmoney+orderproduct["productnumber"]*orderproduct["price"]
            buyprice = buyprice + orderproduct["productnumber"] * productmodel.buyprice
            #封装订单商品集合
            if productmodel.fk_supplierid in supplierid:
               detail= reqOrderSupplierdict[productmodel.fk_supplierid]
               productList=detail["productList"]
               reqOrderSuppliermodel={}
               reqOrderSuppliermodel["totalmoney"]=detail["totalmoney"]+orderproduct["productnumber"]*orderproduct["price"]
               reqOrderSuppliermodel["buymoney"] = detail["buymoney"] + orderproduct["productnumber"] * productmodel.buyprice
               reqOrderSuppliermodel["productList"] = productList.append(orderproduct)
               reqOrderSupplierdict[productmodel.fk_supplierid]=reqOrderSuppliermodel
            else:
                money=orderproduct["productnumber"]*orderproduct["price"]
                buymoney = orderproduct["productnumber"] * productmodel.buyprice
                productList=[]
                productList.append(orderproduct)
                reqOrderSuppliermodel={"buymoney":buymoney,"totalmoney":money,"productList":productList}
                reqOrderSupplierdict[productmodel.fk_supplierid]=reqOrderSuppliermodel
                supplierid.append(productmodel.fk_supplierid)
            #红包可以使用的商品
            if discount is not None:
                if discount.fk_productcolumnsid>0:#商品分类
                   typelist= models.TProductTypebrand.objects.filter(fk_producttypeid=discount.fk_productcolumnsid)
                   if typelist.count()>0:
                       walletmoney=walletmoney+orderproduct["productnumber"]*orderproduct["price"]
                       walletproduct.append(productmodel.id)
                elif discount.fk_promotionsmoduleid>0:#活动模块
                    model1=models.TPromotionsModule.objects.filter(fk_moduleid=discount.fk_promotionsmoduleid)
                    if model1.count()>0:
                        model2=models.TPromotionsNews.objects.filter(promotionsproductid=productmodel.id,fk_pmoduleid=model1[0].id)
                        if model2.count()>0:
                            walletmoney = walletmoney + orderproduct["productnumber"] * orderproduct["price"]
                            walletproduct.append(productmodel.id)
                elif discount.fk_promotionsid>0:#活动
                    model1=models.TPromotions.objects.filter(id=discount.fk_promotionsid)
                    if model1.count()>0:
                        model2=models.TPromotionsModule.objects.filter(id=model1[0].fk_moduleid)
                        for mitem in model2:
                            model3 = models.TPromotionsNews.objects.filter(promotionsproductid=productmodel.id,
                                                                           fk_pmoduleid=mitem.id)
                            if model3.count()>0:
                                walletmoney = walletmoney + orderproduct["productnumber"] * orderproduct["price"]
                                walletproduct.append(productmodel.id)
                                break
                elif discount.isallproduct=="0":
                    walletmoney = walletmoney + orderproduct["productnumber"] * orderproduct["price"]
                    walletproduct.append(productmodel.id)
                    break

        else:
            return {"state":0}
     if discount is not None and walletmoney >= discount.discountsumprice:
         totalmoney = totalmoney - discount.discountdecproce
     if totalmoney == sumprice:
         return {"state":1,"totalmoney":totalmoney,"buyprice":buyprice,"walletmoney":walletmoney,"walletproduct":walletproduct,"reqOrderSupplierdict":reqOrderSupplierdict}
     else:
         return {"state": 0}
def insertorder(wallet,addr,userid,sumprice,discount,walletid,buyprice,reqOrderSupplierdict,walletproduct,walletmoney,allproductlist):
    specialmoney=0
    totalmoney=sumprice
    ordercode=uuid.uuid1()
    if discount is not None:
        wall=walletid
        specialmoney=discount.discountdecproce
        totalmoney=sumprice-specialmoney
    with transaction.atomic():
      ordertotal=  models.TOrdersTotal.objects.create(telephone=addr.telephone, private=addr.privice, address=addr.address,
                                            area=addr.area,city=addr.city,contactname=addr.contactname,email="",fk_memberid=userid,paystate="0",
                                            remark="",isneed="0",ordercode=ordercode,ordertime=datetime.datetime.now(),ordertotalmoney=sumprice,
                                            fk_walletid=wall,specialmoney=specialmoney,totalmoney=totalmoney,buytotalmoney=buyprice)
      i=0
      j=10
      sep=0
      count=len(walletproduct)
      for key in reqOrderSupplierdict:
          supplierid=key
          orderSupplierdict=reqOrderSupplierdict[key]
          stotalmoney=orderSupplierdict["totalmoney"]
          sbuymoney=orderSupplierdict["buymoney"]
          productlist=orderSupplierdict["productList"]
          ordersupplier= models.TOrdersSupplier.objects.create(fk_orderstotalid=ordertotal.id,fk_supplierid=supplierid,orderstatus="0",ordercode=ordercode+j,remark="",totalmoney=stotalmoney,buytotalmoney=sbuymoney,specialmoney=0,actualpaymoney=0)
          j=j+1
          special=0
          specialmoneys=0
          for product in productlist:
              specialmoney1=0
              productmodel = allproductlist.get(id=product["productid"])
              if count > 0 and discount is not None :
                  for walletproductkey in walletproduct:
                      if walletproductkey==productmodel.id:
                              yh = discount.discountdecproce
                              if count - i == 1:
                                  if yh - sep <= 0:
                                      specialmoney1 = 0
                                  else:
                                      specialmoney1 = yh - sep;
                                      special = special + (yh - sep)

                      else:
                          sm = (yh / walletmoney) * product["productnumber"] * product["price"]
                          sm = round(sm, 2)
                          if sep + sm > yh and sep <= yh:
                              specialmoney1 = yh - sep
                              special = special + (yh - sep)
                          elif sep + sm <= yh:
                              specialmoney1 = sm
                              special = special + sm
                          else:
                              specialmoney1 = 0
                          sep = sep + sm
                      i=i+1
              specialmoneys=specialmoneys+specialmoney1
              acpaymoney=product["productnumber"]*productmodel.currentsaleprice-specialmoney1
              intotalmoney=product["productnumber"]*productmodel.currentsaleprice
              inbuymoney=product["productnumber"]*productmodel.buyprice
              models.TOrdersInfo.objects.create(fk_productid=product["productid"],fk_commissiontypeid=productmodel.fk_commissiontypeid,saleprice=productmodel.currentsaleprice,buyprice=productmodel.buyprice,
                                                ratio=0,specialmoney=specialmoney1,actualpaymoney=acpaymoney,buynumber=product["productnumber"],commentstatus="0",remark="",
                                                totalmoney=intotalmoney,buytotalmoney=inbuymoney,fk_orderssupplierid=ordersupplier.id)
              ordersupplier.specialmoney=specialmoneys
              ordersupplier.actualpaymoney=ordersupplier.totalmoney-specialmoneys
              ordersupplier.save()
              productmodel.stocknumber = productmodel.stocknumber - product["productnumber"]
              if productmodel.stocknumber==0:
                  productmodel.status="4"
              productmodel.save()
              #删除购物车
              mm=models.TMemberShoppingcar.objects.filter(fk_productid=productmodel.id,fk_memberid=userid)
              if mm.count()>0:
                  car=mm[0]
                  car.state="2"
                  car.save()

              if wallet is not None:
                  wallet.state=2
                  wallet.save()
              return ordertotal.ordercode
@csrf_exempt
def pay(request):
    response_data={"state":1}
    try:
        jsondata=json.loads(request.body)
        tradetype=jsondata["tradetype"]
        paytype = jsondata["paytype"]
        if tradetype=="APP" and paytype=="1":#微信
              a=1
        elif tradetype=="APP" and paytype=="2":#支付宝
              a=2
        else:
              a=3

    except:
        c1.error()
        response_data["message"]="内部服务器错误"
    return HttpResponse(json.dumps(response_data,ensure_ascii=False))
def wxapppay(outtradeno,deviceinfo,openid,productid,tradetype):
   ordertotallist= models.TOrdersTotal.objects.filter(ordercode=outtradeno)
   if ordertotallist.count()>0:
       ordertotal=ordertotallist[0]
       if ordertotal.paystate=="1":
           return "订单已支付完成"
       else:
           return ""
   else:
       return "订单不存在"
