from django.db import models
#获取首页商品
class FirstpageProductManager(models.Manager):
    def __init__(self,productid):
        self.productid=productid
    def with_counts(self):
        from django.db import connection
        cursor = connection.cursor()
        var1 = self.productid
        cursor.execute("""select a.ID,a.Name from yanwoo.t_product_type as a,yanwoo.t_product_typebrand as b,yanwoo.t_product as c where c.ID= %s and b.FK_ProductBrandID=c.FK_ProductTypeBrandID and b.FK_ProductTypeID=a.ID""",[var1])
        tuple=cursor.fetchall()
        result_dict = {}
        for row in tuple:
            result_dict={"id":row[0],"name":row[1]}
        return result_dict
#获取商品属性
class ProductAttributeManager(models.Manager):
    def __init__(self,productid):
        self.productid=productid
    def queryAttribute(self):
        from django.db import connection
        cursor = connection.cursor()
        var1 = self.productid
        cursor.execute("""select c.groupname,d.attributename,a.othervalue from yanwoo.t_product_attribute as a,yanwoo.T_AttributeGroups_Relate as b,yanwoo.T_Attribute_Groups as c,yanwoo.T_Attribute as d where a.FK_ProductID=%s and a.FK_AttributeGroupsRelateID=b.ID and b.FK_AttributeGroupsID=c.ID and b.FK_AttributeID=d.ID""",[var1])
        tuple=cursor.fetchall()
        list = []
        for row in tuple:
            result_dict={"groupname":row[0],"attributename":row[1],"othervalue":row[2]}
            list.append(result_dict)
        return list
#得到商品根据商品分类
class GetProductByTypeidManager(models.Manager):
    def __init__(self,producttypeid,startindex,endindex):
        self.producttypeid=producttypeid
        self.startindex=startindex
        self.endindex=endindex
    def queryProduct(self):
        from django.db import connection
        cursor = connection.cursor()
        var1 = self.producttypeid
        var2 = self.startindex
        var3= self.endindex
        cursor.execute("""select a.* from yanwoo.t_product as a,yanwoo.T_Product_TypeBrand as b where b.FK_ProductTypeID=%s and b.ID=a.FK_ProductTypeBrandID and a.status='3' order by a.salenumber desc limit %s,%s """,[var1,var2,var3])
        tuple=cursor.fetchall()
        return tuple