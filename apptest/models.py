# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class LsUser(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=11, blank=True, null=True)
    user_password = models.CharField(max_length=128, blank=True, null=True)
    user_nikename = models.CharField(max_length=30, blank=True, null=True)
    user_head_img = models.TextField(blank=True, null=True)
    user_phone = models.CharField(max_length=11, blank=True, null=True)
    user_sex = models.CharField(max_length=3, blank=True, null=True)
    user_area = models.CharField(max_length=10, blank=True, null=True)
    user_money = models.FloatField(blank=True, null=True)
    user_level = models.IntegerField(blank=True, null=True)
    user_last_time = models.CharField(max_length=50, blank=True, null=True)
    user_create_time = models.DateTimeField()
    zhifubao = models.CharField(max_length=11, blank=True, null=True)
    weixin = models.CharField(max_length=20, blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ls_user'


class TAppSpread(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_app_spread'


class TAppVersion(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=20, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=100, blank=True, null=True)  # Field name made lowercase.
    islimit = models.CharField(db_column='IsLimit', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fk_userid = models.IntegerField(db_column='FK_UserID', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_app_version'


class TAttribute(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    attributecode = models.CharField(db_column='AttributeCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    attributename = models.CharField(db_column='AttributeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isfilter = models.CharField(db_column='IsFilter', max_length=1, blank=True, null=True)  # Field name made lowercase.
    issallattribute = models.CharField(db_column='IsSallAttribute', max_length=1, blank=True, null=True)  # Field name made lowercase.
    iskeyattribute = models.CharField(db_column='IsKeyAttribute', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    sign = models.CharField(db_column='Sign', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_attribute'


class TAttributeGroups(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_producttypeid = models.IntegerField(db_column='FK_ProductTypeID', blank=True, null=True)  # Field name made lowercase.
    groupcode = models.CharField(db_column='GroupCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    sign = models.CharField(db_column='Sign', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_attribute_groups'


class TAttributeValues(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_attributeid = models.IntegerField(db_column='FK_AttributeID', blank=True, null=True)  # Field name made lowercase.
    attributevaluecode = models.CharField(db_column='AttributeValueCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    attributevalue = models.CharField(db_column='AttributeValue', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isinput = models.CharField(db_column='IsInput', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    sign = models.CharField(db_column='Sign', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_attribute_values'


class TAttributegroupsRelate(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_attributegroupsid = models.IntegerField(db_column='FK_AttributeGroupsID', blank=True, null=True)  # Field name made lowercase.
    fk_attributeid = models.IntegerField(db_column='FK_AttributeID', blank=True, null=True)  # Field name made lowercase.
    isfilter = models.CharField(db_column='IsFilter', max_length=1, blank=True, null=True)  # Field name made lowercase.
    issallattribute = models.CharField(db_column='IsSallAttribute', max_length=1, blank=True, null=True)  # Field name made lowercase.
    iskeyattribute = models.CharField(db_column='IsKeyAttribute', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_attributegroups_relate'


class TCommissionType(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ratio = models.FloatField(db_column='Ratio', blank=True, null=True)  # Field name made lowercase.
    sign = models.CharField(db_column='Sign', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_commission_type'


class TCreditsInfo(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    creditsruleid = models.IntegerField(db_column='CreditsRuleID', blank=True, null=True)  # Field name made lowercase.
    creditsvalue = models.IntegerField(db_column='CreditsValue', blank=True, null=True)  # Field name made lowercase.
    creditsrulecontent = models.CharField(db_column='CreditsRuleContent', max_length=100, blank=True, null=True)  # Field name made lowercase.
    creditsdatetime = models.DateTimeField(db_column='CreditsDateTime')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_credits_info'


class TCreditsRule(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    rulename = models.CharField(db_column='RuleName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    creditsrulecontent = models.CharField(db_column='CreditsRuleContent', max_length=100, blank=True, null=True)  # Field name made lowercase.
    creditsvalue = models.IntegerField(db_column='CreditsValue', blank=True, null=True)  # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='CreateDateTime')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_credits_rule'


class TDiscount(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    discountcode = models.CharField(db_column='DiscountCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    discountname = models.CharField(db_column='DiscountName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    discountintro = models.CharField(db_column='Discountintro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discountsumprice = models.FloatField(db_column='DiscountSumPrice', blank=True, null=True)  # Field name made lowercase.
    discountdecproce = models.FloatField(db_column='DiscountDecProce', blank=True, null=True)  # Field name made lowercase.
    sendmode = models.IntegerField(db_column='SendMode', blank=True, null=True)  # Field name made lowercase.
    getmode = models.IntegerField(db_column='GetMode', blank=True, null=True)  # Field name made lowercase.
    isallproduct = models.CharField(db_column='IsAllProduct', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fk_productcolumnsid = models.IntegerField(db_column='FK_ProductColumnsID', blank=True, null=True)  # Field name made lowercase.
    fk_promotionsid = models.IntegerField(db_column='FK_PromotionsID', blank=True, null=True)  # Field name made lowercase.
    fk_promotionsmoduleid = models.IntegerField(db_column='FK_PromotionsModuleID', blank=True, null=True)  # Field name made lowercase.
    discountstartdatetime = models.DateTimeField(db_column='DiscountStartDateTime')  # Field name made lowercase.
    discountenddatetime = models.DateTimeField(db_column='DiscountEndDateTime')  # Field name made lowercase.
    getstartdatetime = models.DateTimeField(db_column='GetStartDateTime')  # Field name made lowercase.
    getenddatetime = models.DateTimeField(db_column='GetEndDateTime')  # Field name made lowercase.
    discountcount = models.IntegerField(db_column='DiscountCount', blank=True, null=True)  # Field name made lowercase.
    discountpageurl = models.CharField(db_column='DiscountPageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fk_applyuserid = models.IntegerField(db_column='FK_ApplyUserID', blank=True, null=True)  # Field name made lowercase.
    applydatetime = models.DateTimeField(db_column='ApplyDateTime')  # Field name made lowercase.
    fk_checkuserid = models.IntegerField(db_column='FK_CheckUserID', blank=True, null=True)  # Field name made lowercase.
    checkdatetime = models.DateTimeField(db_column='CheckDateTime')  # Field name made lowercase.
    checkstatus = models.IntegerField(db_column='CheckStatus', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remaincount = models.IntegerField(db_column='RemainCount', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_discount'


class TExperiencestore(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    storename = models.CharField(db_column='StoreName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    introduction = models.TextField(db_column='Introduction', blank=True, null=True)  # Field name made lowercase.
    provice = models.CharField(db_column='Provice', max_length=6, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    linkman = models.CharField(db_column='LinkMan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    linktelphone = models.CharField(db_column='LinkTelphone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    images = models.CharField(db_column='Images', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storecode = models.IntegerField(db_column='StoreCode', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=6, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=6, blank=True, null=True)  # Field name made lowercase.
    fk_userid = models.IntegerField(db_column='FK_UserID', blank=True, null=True)  # Field name made lowercase.
    provicename = models.CharField(db_column='ProviceName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cityname = models.CharField(db_column='CityName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    accountday = models.CharField(db_column='AccountDay', max_length=10, blank=True, null=True)  # Field name made lowercase.
    areaname = models.CharField(db_column='AreaName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    joiningdate = models.CharField(db_column='JoiningDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    entertime = models.DateTimeField(db_column='EnterTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_experiencestore'


class TFeedback(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_userid = models.IntegerField(db_column='Fk_Userid', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_feedback'

class TFirstpageProducttype(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    typecode = models.IntegerField(db_column='TypeCode', blank=True, null=True)  # Field name made lowercase.
    typename = models.CharField(db_column='TypeName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    num = models.IntegerField(db_column='Num', blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    # 与Publish建立一对多的关系,外键字段建立在多的一方

    class Meta:
        #managed = False
        ordering = ['sort']
        db_table = 't_firstpage_producttype'

class TFirstpageProduct(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_type = models.IntegerField(db_column='FK_Type', blank=True, null=True)  # Field name made lowercase.
    fk_product = models.IntegerField(db_column='Fk_Product', blank=True, null=True)  # Field name made lowercase.
    img = models.CharField(db_column='Img', max_length=100, blank=True, null=True)  # Field name made lowercase.
    head = models.CharField(db_column='Head', max_length=100, blank=True, null=True)  # Field name made lowercase.
    descs = models.CharField(db_column='Descs', max_length=255, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=1, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    product_saleprice = models.FloatField(db_column='Product_SalePrice', blank=True, null=True)  # Field name made lowercase.
    #fk_product = models.ForeignKey("TFirstpageProducttype",on_delete=models.BooleanField)
    class Meta:
        #managed = False
        ordering = ['sort']
        db_table = 't_firstpage_product'


class TGifts(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    giftsname = models.CharField(db_column='GiftsName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    giftsintro = models.CharField(db_column='GiftsIntro', max_length=100, blank=True, null=True)  # Field name made lowercase.
    giftsproductid = models.IntegerField(db_column='GiftsProductID', blank=True, null=True)  # Field name made lowercase.
    shoppingsumprice = models.FloatField(db_column='ShoppingSumPrice', blank=True, null=True)  # Field name made lowercase.
    isallproduct = models.IntegerField(db_column='IsAllProduct', blank=True, null=True)  # Field name made lowercase.
    productcolumnsid = models.IntegerField(db_column='ProductColumnsID', blank=True, null=True)  # Field name made lowercase.
    promotionsid = models.IntegerField(db_column='PromotionsID', blank=True, null=True)  # Field name made lowercase.
    promotionsmoduleid = models.IntegerField(db_column='PromotionsModuleID', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate')  # Field name made lowercase.
    fk_applyuserid = models.IntegerField(db_column='FK_ApplyUserID', blank=True, null=True)  # Field name made lowercase.
    applydatetime = models.DateTimeField(db_column='ApplyDateTime')  # Field name made lowercase.
    checkuserid = models.IntegerField(db_column='CheckUserID', blank=True, null=True)  # Field name made lowercase.
    checkdatetime = models.DateTimeField(db_column='CheckDateTime')  # Field name made lowercase.
    checkstatus = models.IntegerField(db_column='CheckStatus', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_gifts'


class TGiftsProduct(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_giftsid = models.IntegerField(db_column='FK_GiftsID', blank=True, null=True)  # Field name made lowercase.
    fk_productid = models.IntegerField(db_column='FK_ProductID', blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_gifts_product'


class TLogisticsinfo(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_logisticsinfo'


class TLogisticssupplier(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_supplierid = models.IntegerField(db_column='FK_SupplierID', blank=True, null=True)  # Field name made lowercase.
    fk_logisticsinfoid = models.IntegerField(db_column='FK_LogisticsInfoID', blank=True, null=True)  # Field name made lowercase.
    linkman = models.CharField(db_column='Linkman', max_length=20, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_logisticssupplier'


class tmember(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='NickName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    headpath = models.CharField(db_column='HeadPath', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='TelePhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phoneid = models.CharField(db_column='PhoneID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=1, blank=True, null=True)  # Field name made lowercase.
    birthday = models.CharField(db_column='Birthday', max_length=10, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=20, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    logintime = models.DateTimeField(db_column='LoginTime')  # Field name made lowercase.
    appchannelinfoid = models.IntegerField(db_column='AppChannelInfoID', blank=True, null=True)  # Field name made lowercase.
    credits = models.IntegerField(db_column='Credits', blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fk_experiencestoreid = models.IntegerField(db_column='FK_ExperienceStoreID', blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=20, blank=True, null=True)  # Field name made lowercase.
    belongtime = models.DateTimeField(db_column='BelongTime')  # Field name made lowercase.
    clientostype = models.CharField(db_column='ClientOSType', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmember'


class TMemberBrowse(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_productid = models.IntegerField(db_column='FK_ProductID', blank=True, null=True)  # Field name made lowercase.
    fk_memberid = models.IntegerField(db_column='FK_MemberID', blank=True, null=True)  # Field name made lowercase.
    fk_supplierid = models.IntegerField(db_column='FK_SupplierID', blank=True, null=True)  # Field name made lowercase.
    browernumber = models.IntegerField(db_column='BrowerNumber', blank=True, null=True)  # Field name made lowercase.
    lastbrowsedatetime = models.DateTimeField(db_column='LastBrowseDateTime')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_member_browse'


class TMemberCollection(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_memberid = models.IntegerField(db_column='FK_MemberID', blank=True, null=True)  # Field name made lowercase.
    fk_productid = models.IntegerField(db_column='FK_ProductID', blank=True, null=True)  # Field name made lowercase.
    collectiondatetime = models.DateTimeField(db_column='CollectionDateTime')  # Field name made lowercase.
    collectionstatus = models.CharField(db_column='CollectionStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_member_collection'


class TMemberContact(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_memberid = models.IntegerField(db_column='FK_MemberID', blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    privice = models.CharField(db_column='Privice', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    default = models.IntegerField(db_column='Default', blank=True, null=True)  # Field name made lowercase.
    provicecode = models.CharField(db_column='ProviceCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    citycode = models.CharField(db_column='CityCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    entertime = models.DateTimeField(db_column='EnterTime')  # Field name made lowercase.
    isdel = models.CharField(db_column='IsDel', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_member_contact'


class TMemberInvoice(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_memberid = models.IntegerField(db_column='FK_MemberID', blank=True, null=True)  # Field name made lowercase.
    fk_invoicetypeid = models.IntegerField(db_column='FK_InvoiceTypeID', blank=True, null=True)  # Field name made lowercase.
    invoicename = models.CharField(db_column='InvoiceName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fk_invoicecontentid = models.IntegerField(db_column='FK_InvoiceContentID', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_member_invoice'


class TMemberProductremind(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_promotionsid = models.IntegerField(db_column='FK_PromotionsID', blank=True, null=True)  # Field name made lowercase.
    fk_productid = models.IntegerField(db_column='FK_ProductID', blank=True, null=True)  # Field name made lowercase.
    fk_memberid = models.IntegerField(db_column='FK_MemberID', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_member_productremind'


class TMemberSearch(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_memberid = models.IntegerField(db_column='FK_MemberID', blank=True, null=True)  # Field name made lowercase.
    searchkeyword = models.CharField(db_column='SearchKeyword', max_length=100, blank=True, null=True)  # Field name made lowercase.
    searchdatetime = models.DateTimeField(db_column='SearchDateTime')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_member_search'


class TMemberShoppingcar(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_memberid = models.IntegerField(db_column='FK_MemberID', blank=True, null=True)  # Field name made lowercase.
    fk_productid = models.IntegerField(db_column='FK_ProductID', blank=True, null=True)  # Field name made lowercase.
    fk_supplierid = models.IntegerField(db_column='FK_SupplierID', blank=True, null=True)  # Field name made lowercase.
    productnumber = models.IntegerField(db_column='ProductNumber', blank=True, null=True)  # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='CreateDateTime')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_member_shoppingcar'


class TMemberWallet(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_member = models.IntegerField(db_column='Fk_Member', blank=True, null=True)  # Field name made lowercase.
    fk_discount = models.IntegerField(db_column='Fk_Discount', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_member_wallet'


class TModule(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    modulename = models.CharField(db_column='ModuleName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    moduledesc = models.CharField(db_column='ModuleDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    moduleimg = models.CharField(db_column='ModuleImg', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isneedtitle = models.CharField(db_column='IsNeedTitle', max_length=1, blank=True, null=True)  # Field name made lowercase.
    isneedintro = models.CharField(db_column='IsNeedIntro', max_length=1, blank=True, null=True)  # Field name made lowercase.
    isneedlink = models.CharField(db_column='IsNeedLink', max_length=1, blank=True, null=True)  # Field name made lowercase.
    isneedcontent = models.CharField(db_column='IsNeedContent', max_length=1, blank=True, null=True)  # Field name made lowercase.
    isneedproduct = models.CharField(db_column='IsNeedProduct', max_length=1, blank=True, null=True)  # Field name made lowercase.
    isneedimage = models.CharField(db_column='IsNeedImage', max_length=1, blank=True, null=True)  # Field name made lowercase.
    modulecode = models.TextField(db_column='ModuleCode', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_module'


class TOrdersComment(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_memberid = models.IntegerField(db_column='FK_MemberID', blank=True, null=True)  # Field name made lowercase.
    fk_productid = models.IntegerField(db_column='FK_ProductID', blank=True, null=True)  # Field name made lowercase.
    fk_orders_infoid = models.IntegerField(db_column='FK_Orders_InfoID', blank=True, null=True)  # Field name made lowercase.
    commentcontent = models.CharField(db_column='CommentContent', max_length=255, blank=True, null=True)  # Field name made lowercase.
    commentimglist = models.CharField(db_column='CommentImgList', max_length=255, blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    commenttime = models.DateTimeField(db_column='CommentTime')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_orders_comment'


class TOrdersInfo(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_orderssupplierid = models.IntegerField(db_column='FK_OrdersSupplierID', blank=True, null=True)  # Field name made lowercase.
    fk_productid = models.IntegerField(db_column='FK_ProductID', blank=True, null=True)  # Field name made lowercase.
    buynumber = models.IntegerField(db_column='BuyNumber', blank=True, null=True)  # Field name made lowercase.
    saleprice = models.FloatField(db_column='SalePrice', blank=True, null=True)  # Field name made lowercase.
    specialmoney = models.FloatField(db_column='SpecialMoney', blank=True, null=True)  # Field name made lowercase.
    totalmoney = models.FloatField(db_column='TotalMoney', blank=True, null=True)  # Field name made lowercase.
    commentstatus = models.CharField(db_column='CommentStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    actualpaymoney = models.FloatField(db_column='ActualPayMoney', blank=True, null=True)  # Field name made lowercase.
    ratio = models.FloatField(db_column='Ratio', blank=True, null=True)  # Field name made lowercase.
    buyprice = models.FloatField(db_column='BuyPrice', blank=True, null=True)  # Field name made lowercase.
    buytotalmoney = models.FloatField(db_column='BuyTotalMoney', blank=True, null=True)  # Field name made lowercase.
    fk_commissiontypeid = models.IntegerField(db_column='FK_CommissionTypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_orders_info'


class TOrdersSupplier(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_orderstotalid = models.IntegerField(db_column='FK_OrdersTotalID', blank=True, null=True)  # Field name made lowercase.
    fk_supplierid = models.IntegerField(db_column='FK_SupplierID', blank=True, null=True)  # Field name made lowercase.
    ordercode = models.CharField(db_column='OrderCode', max_length=40, blank=True, null=True)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    couriernumber = models.CharField(db_column='CourierNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    couriercompany = models.CharField(db_column='CourierCompany', max_length=20, blank=True, null=True)  # Field name made lowercase.
    senddatetime = models.DateTimeField(db_column='SendDateTime')  # Field name made lowercase.
    totalmoney = models.FloatField(db_column='TotalMoney', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    couriercompanyname = models.CharField(db_column='CourierCompanyName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    acceptdatetime = models.DateTimeField(db_column='AcceptDateTime')  # Field name made lowercase.
    fk_sendsupplierid = models.IntegerField(db_column='Fk_SendSupplierID', blank=True, null=True)  # Field name made lowercase.
    acceptway = models.CharField(db_column='AcceptWay', max_length=1, blank=True, null=True)  # Field name made lowercase.
    specialmoney = models.FloatField(db_column='SpecialMoney', blank=True, null=True)  # Field name made lowercase.
    buytotalmoney = models.FloatField(db_column='BuyTotalMoney', blank=True, null=True)  # Field name made lowercase.
    actualpaymoney = models.FloatField(db_column='ActualPayMoney', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_orders_supplier'


class TOrdersTotal(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_memberid = models.IntegerField(db_column='FK_MemberID', blank=True, null=True)  # Field name made lowercase.
    ordercode = models.CharField(db_column='OrderCode', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ordertotalmoney = models.FloatField(db_column='OrderTotalMoney', blank=True, null=True)  # Field name made lowercase.
    fk_walletid = models.IntegerField(db_column='FK_WalletID', blank=True, null=True)  # Field name made lowercase.
    ordertime = models.DateTimeField(db_column='OrderTime')  # Field name made lowercase.
    paytype = models.CharField(db_column='PayType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    paystate = models.CharField(db_column='PayState', max_length=1, blank=True, null=True)  # Field name made lowercase.
    payovertime = models.DateTimeField(db_column='PayOverTime')  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    private = models.CharField(db_column='Private', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=20, blank=True, null=True)  # Field name made lowercase.
    invoicetype = models.CharField(db_column='InvoiceType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    invoicename = models.CharField(db_column='InvoiceName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    invoicecontent = models.CharField(db_column='InvoiceContent', max_length=20, blank=True, null=True)  # Field name made lowercase.
    isneed = models.CharField(db_column='IsNeed', max_length=1, blank=True, null=True)  # Field name made lowercase.
    payordercode = models.CharField(db_column='PayOrderCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mchid = models.CharField(db_column='MchID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    openid = models.CharField(db_column='OpenID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deviceinfo = models.CharField(db_column='DeviceInfo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    totalmoney = models.FloatField(db_column='TotalMoney', blank=True, null=True)  # Field name made lowercase.
    buytotalmoney = models.FloatField(db_column='BuyTotalMoney', blank=True, null=True)  # Field name made lowercase.
    specialmoney = models.FloatField(db_column='SpecialMoney', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_orders_total'


class TProduct(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_supplierid = models.IntegerField(db_column='FK_SupplierID', blank=True, null=True)  # Field name made lowercase.
    fk_producttypebrandid = models.IntegerField(db_column='FK_ProductTypeBrandID', blank=True, null=True)  # Field name made lowercase.
    productcode = models.CharField(db_column='ProductCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    productdesc = models.CharField(db_column='ProductDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tagids = models.CharField(db_column='TagIDs', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saleprice = models.FloatField(db_column='SalePrice', blank=True, null=True)  # Field name made lowercase.
    buyprice = models.FloatField(db_column='BuyPrice', blank=True, null=True)  # Field name made lowercase.
    currentsaleprice = models.FloatField(db_column='CurrentSalePrice', blank=True, null=True)  # Field name made lowercase.
    stocknumber = models.IntegerField(db_column='StockNumber', blank=True, null=True)  # Field name made lowercase.
    stockguardnumber = models.IntegerField(db_column='StockGuardNumber', blank=True, null=True)  # Field name made lowercase.
    salenumber = models.IntegerField(db_column='SaleNumber', blank=True, null=True)  # Field name made lowercase.
    graphicdetails = models.TextField(db_column='GraphicDetails', blank=True, null=True)  # Field name made lowercase.
    graphicdetailspath = models.CharField(db_column='GraphicDetailsPath', max_length=100, blank=True, null=True)  # Field name made lowercase.
    formatdetails = models.TextField(db_column='FormatDetails', blank=True, null=True)  # Field name made lowercase.
    service = models.TextField(db_column='Service', blank=True, null=True)  # Field name made lowercase.
    browsenumber = models.IntegerField(db_column='BrowseNumber', blank=True, null=True)  # Field name made lowercase.
    collectionnumber = models.IntegerField(db_column='CollectionNumber', blank=True, null=True)  # Field name made lowercase.
    enteruserid = models.IntegerField(db_column='EnterUserID', blank=True, null=True)  # Field name made lowercase.
    entertime = models.DateTimeField(db_column='EnterTime')  # Field name made lowercase.
    updateuserid = models.IntegerField(db_column='UpdateUserID', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime')  # Field name made lowercase.
    auditinguserid = models.IntegerField(db_column='AuditingUserID', blank=True, null=True)  # Field name made lowercase.
    auditingdesc = models.CharField(db_column='AuditingDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    auditingtime = models.DateTimeField(db_column='AuditingTime')  # Field name made lowercase.
    putawaytime = models.DateTimeField(db_column='PutawayTime')  # Field name made lowercase.
    outawaytime = models.DateTimeField(db_column='OutawayTime')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fk_commissiontypeid = models.IntegerField(db_column='FK_CommissionTypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_product'


class TProductApplyprice(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_productid = models.IntegerField(db_column='FK_ProductID', blank=True, null=True)  # Field name made lowercase.
    fk_commissiontypeid = models.IntegerField(db_column='FK_CommissionTypeID', blank=True, null=True)  # Field name made lowercase.
    currentsaleprice = models.FloatField(db_column='CurrentSalePrice', blank=True, null=True)  # Field name made lowercase.
    currentbuyprice = models.FloatField(db_column='CurrentBuyPrice', blank=True, null=True)  # Field name made lowercase.
    applysaleprice = models.FloatField(db_column='ApplySalePrice', blank=True, null=True)  # Field name made lowercase.
    applybuyprice = models.FloatField(db_column='ApplyBuyPrice', blank=True, null=True)  # Field name made lowercase.
    applystarttime = models.DateTimeField(db_column='ApplyStartTime')  # Field name made lowercase.
    applyendtime = models.DateTimeField(db_column='ApplyEndTime')  # Field name made lowercase.
    applyuserid = models.IntegerField(db_column='ApplyUserID', blank=True, null=True)  # Field name made lowercase.
    applydatetime = models.DateTimeField(db_column='ApplyDateTime')  # Field name made lowercase.
    updateuserid = models.IntegerField(db_column='UpdateUserID', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime')  # Field name made lowercase.
    auditinguserid = models.IntegerField(db_column='AuditingUserID', blank=True, null=True)  # Field name made lowercase.
    auditingdesc = models.CharField(db_column='AuditingDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    auditingtime = models.DateTimeField(db_column='AuditingTime')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    isupdate = models.CharField(db_column='IsUpdate', max_length=1, blank=True, null=True)  # Field name made lowercase.
    isreturn = models.CharField(db_column='IsReturn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_product_applyprice'


class TProductAttribute(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_productid = models.IntegerField(db_column='FK_ProductID', blank=True, null=True)  # Field name made lowercase.
    fk_attributegroupsrelateid = models.IntegerField(db_column='FK_AttributeGroupsRelateID', blank=True, null=True)  # Field name made lowercase.
    attributevaluesid = models.IntegerField(db_column='AttributeValuesID', blank=True, null=True)  # Field name made lowercase.
    othervalue = models.CharField(db_column='OtherValue', max_length=200, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_product_attribute'


class TProductBrand(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    brandcode = models.CharField(db_column='BrandCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    brandname = models.CharField(db_column='BrandName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sign = models.CharField(db_column='Sign', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_product_brand'


class TProductImages(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_productid = models.IntegerField(db_column='FK_ProductID', blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ismain = models.CharField(db_column='IsMain', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_product_images'


class TProductSku(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    skucode = models.CharField(db_column='SKUCode', max_length=40, blank=True, null=True)  # Field name made lowercase.
    fk_productid = models.IntegerField(db_column='FK_ProductID', blank=True, null=True)  # Field name made lowercase.
    fk_attributeid = models.IntegerField(db_column='FK_AttributeID', blank=True, null=True)  # Field name made lowercase.
    attributevalue = models.CharField(db_column='AttributeValue', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_product_sku'


class TProductTags(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_productid = models.IntegerField(db_column='FK_ProductID', blank=True, null=True)  # Field name made lowercase.
    fk_tagid = models.IntegerField(db_column='FK_TagID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_product_tags'


class TProductType(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fatherid = models.IntegerField(db_column='FatherID', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imagename = models.CharField(db_column='ImageName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pricerange = models.CharField(db_column='PriceRange', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grade = models.IntegerField(db_column='Grade', blank=True, null=True)  # Field name made lowercase.
    ischildren = models.CharField(db_column='isChildren', max_length=1, blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    sign = models.CharField(db_column='Sign', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_product_type'


class TProductTypebrand(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_producttypeid = models.IntegerField(db_column='FK_ProductTypeID', blank=True, null=True)  # Field name made lowercase.
    fk_productbrandid = models.IntegerField(db_column='FK_ProductBrandID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_product_typebrand'


class TPromotions(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    promotionsname = models.CharField(db_column='PromotionsName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    promotionsdesc = models.CharField(db_column='PromotionsDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    promotionsimg = models.CharField(db_column='PromotionsImg', max_length=100, blank=True, null=True)  # Field name made lowercase.
    promotionsbgcolor = models.CharField(db_column='PromotionsBgColor', max_length=10, blank=True, null=True)  # Field name made lowercase.
    promotionsbgimage = models.CharField(db_column='PromotionsBgImage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    promotionsstartdatetime = models.DateTimeField(db_column='PromotionsStartDateTime')  # Field name made lowercase.
    promotionsenddatetime = models.DateTimeField(db_column='PromotionsEndDateTime')  # Field name made lowercase.
    fk_applyuserid = models.IntegerField(db_column='FK_ApplyUserID', blank=True, null=True)  # Field name made lowercase.
    applydatetime = models.DateTimeField(db_column='ApplyDateTime')  # Field name made lowercase.
    checkuserid = models.IntegerField(db_column='CheckUserID', blank=True, null=True)  # Field name made lowercase.
    checkdatetime = models.DateTimeField(db_column='CheckDateTime')  # Field name made lowercase.
    promotionsstatus = models.IntegerField(db_column='PromotionsStatus', blank=True, null=True)  # Field name made lowercase.
    promotionspageurl = models.CharField(db_column='PromotionsPageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    promotionscode = models.TextField(db_column='PromotionsCode', blank=True, null=True)  # Field name made lowercase.
    promotionsqrcode = models.CharField(db_column='PromotionsQRCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_promotions'


class TPromotionsModule(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_promotionsid = models.IntegerField(db_column='FK_PromotionsID', blank=True, null=True)  # Field name made lowercase.
    fk_moduleid = models.IntegerField(db_column='FK_ModuleID', blank=True, null=True)  # Field name made lowercase.
    pmodulename = models.CharField(db_column='PModuleName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pmodulesort = models.IntegerField(db_column='PModuleSort', blank=True, null=True)  # Field name made lowercase.
    pmodulecode = models.TextField(db_column='PModuleCode', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_promotions_module'


class TPromotionsNews(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_pmoduleid = models.IntegerField(db_column='FK_PModuleID', blank=True, null=True)  # Field name made lowercase.
    promotionstilte = models.CharField(db_column='PromotionsTilte', max_length=100, blank=True, null=True)  # Field name made lowercase.
    promotionsintro = models.CharField(db_column='PromotionsIntro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    promotionslink = models.CharField(db_column='PromotionsLink', max_length=100, blank=True, null=True)  # Field name made lowercase.
    promotionscontent = models.TextField(db_column='PromotionsContent', blank=True, null=True)  # Field name made lowercase.
    promotionsimage = models.CharField(db_column='PromotionsImage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    promotionsproductid = models.IntegerField(db_column='PromotionsProductID', blank=True, null=True)  # Field name made lowercase.
    promotionssort = models.IntegerField(db_column='PromotionsSort', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_promotions_news'


class TSupplier(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_suppliertypeid = models.IntegerField(db_column='FK_SupplierTypeID', blank=True, null=True)  # Field name made lowercase.
    suppliername = models.CharField(db_column='SupplierName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(db_column='KeyWord', max_length=200, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1, blank=True, null=True)  # Field name made lowercase.
    private = models.CharField(db_column='Private', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    linkman = models.CharField(db_column='Linkman', max_length=20, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bankid = models.CharField(db_column='BankID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bankcard = models.CharField(db_column='BankCard', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bankaddress = models.CharField(db_column='BankAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entertime = models.CharField(db_column='EnterTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='EndTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fk_userid = models.IntegerField(db_column='FK_UserID', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_supplier'


class TSupplierType(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40, blank=True, null=True)  # Field name made lowercase.
    receipttype = models.CharField(db_column='ReceiptType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taxratio = models.FloatField(db_column='TaxRatio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_supplier_type'


class TSysAppchannelinfo(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sign = models.CharField(db_column='Sign', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_appchannelinfo'


class TSysAuth(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    appid = models.CharField(db_column='AppID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    platname = models.CharField(db_column='PlatName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    publickey = models.CharField(db_column='PublicKey', max_length=255, blank=True, null=True)  # Field name made lowercase.
    privatekey = models.CharField(db_column='PrivateKey', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_auth'


class TSysCity(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=6, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    provicecode = models.CharField(db_column='ProviceCode', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_city'


class TSysClientserviceRelate(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_serviceinfoid = models.IntegerField(db_column='FK_ServiceInfoID', blank=True, null=True)  # Field name made lowercase.
    fk_clientversionid = models.IntegerField(db_column='FK_ClientVersionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_clientservice_relate'


class TSysClientversion(models.Model):
  #  id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_userid = models.IntegerField(db_column='FK_UserID', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=20, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=100, blank=True, null=True)  # Field name made lowercase.
    islimit = models.CharField(db_column='IsLimit', max_length=1, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_clientversion'


class TSysCountry(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=6, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fk_citycode = models.CharField(db_column='FK_CityCode', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_country'


class TSysDepartment(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=40, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    departmenthead = models.CharField(db_column='DepartmentHead', max_length=20, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_department'


class TSysInvoicecomment(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    invoicecomment = models.CharField(db_column='InvoiceComment', max_length=30, blank=True, null=True)  # Field name made lowercase.
    suppliertype = models.IntegerField(db_column='SupplierType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_invoicecomment'


class TSysInvoicetype(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    invoicetype = models.CharField(db_column='InvoiceType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    suppliertype = models.IntegerField(db_column='SupplierType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_invoicetype'


class TSysMenu(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=40, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    icons = models.CharField(max_length=40, blank=True, null=True)
    path = models.CharField(db_column='Path', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fatherid = models.IntegerField(db_column='FatherID', blank=True, null=True)  # Field name made lowercase.
    grade = models.IntegerField(db_column='Grade', blank=True, null=True)  # Field name made lowercase.
    ischildren = models.CharField(db_column='isChildren', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sign = models.CharField(db_column='Sign', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_menu'


class TSysMsg(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_msgtypeid = models.IntegerField(db_column='FK_MsgTypeID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=40, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=200, blank=True, null=True)  # Field name made lowercase.
    iconspath = models.CharField(db_column='IconsPath', max_length=100, blank=True, null=True)  # Field name made lowercase.
    msgurl = models.CharField(db_column='MsgUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    issend = models.CharField(db_column='IsSend', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sendtime = models.DateTimeField(db_column='SendTime')  # Field name made lowercase.
    isnew = models.CharField(db_column='IsNew', max_length=1, blank=True, null=True)  # Field name made lowercase.
    islook = models.CharField(db_column='IsLook', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=40, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_msg'


class TSysMsgmycapital(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_msgtypeid = models.IntegerField(db_column='FK_MsgTypeID', blank=True, null=True)  # Field name made lowercase.
    mycapitaltype = models.CharField(db_column='MyCapitalType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fk_walletid = models.IntegerField(db_column='FK_WalletID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=40, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=200, blank=True, null=True)  # Field name made lowercase.
    iconspath = models.CharField(db_column='IconsPath', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    issend = models.CharField(db_column='IsSend', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sendtime = models.DateTimeField(db_column='SendTime')  # Field name made lowercase.
    isnew = models.CharField(db_column='IsNew', max_length=1, blank=True, null=True)  # Field name made lowercase.
    islook = models.CharField(db_column='IsLook', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_msgmycapital'


class TSysMsgorder(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_msgtypeid = models.IntegerField(db_column='FK_MsgTypeID', blank=True, null=True)  # Field name made lowercase.
    fk_orderssupplierid = models.IntegerField(db_column='FK_OrdersSupplierID', blank=True, null=True)  # Field name made lowercase.
    fk_msgordernodeid = models.IntegerField(db_column='FK_MsgOrderNodeID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=40, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=200, blank=True, null=True)  # Field name made lowercase.
    iconspath = models.CharField(db_column='IconsPath', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    issend = models.CharField(db_column='IsSend', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sendtime = models.DateTimeField(db_column='SendTime')  # Field name made lowercase.
    isnew = models.CharField(db_column='IsNew', max_length=1, blank=True, null=True)  # Field name made lowercase.
    islook = models.CharField(db_column='IsLook', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_msgorder'


class TSysMsgordernode(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    nodename = models.CharField(db_column='NodeName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sign = models.CharField(db_column='Sign', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_msgordernode'


class TSysMsgproductremind(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_msgtypeid = models.IntegerField(db_column='FK_MsgTypeID', blank=True, null=True)  # Field name made lowercase.
    fk_memberproductremindid = models.IntegerField(db_column='FK_MemberProductRemindID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=40, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=200, blank=True, null=True)  # Field name made lowercase.
    iconspath = models.CharField(db_column='IconsPath', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    issend = models.CharField(db_column='IsSend', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sendtime = models.DateTimeField(db_column='SendTime')  # Field name made lowercase.
    isnew = models.CharField(db_column='IsNew', max_length=1, blank=True, null=True)  # Field name made lowercase.
    islook = models.CharField(db_column='IsLook', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_msgproductremind'


class TSysMsgpromotions(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_msgtypeid = models.IntegerField(db_column='FK_MsgTypeID', blank=True, null=True)  # Field name made lowercase.
    fk_promotionsid = models.IntegerField(db_column='FK_PromotionsID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=40, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    issend = models.CharField(db_column='IsSend', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sendtime = models.DateTimeField(db_column='SendTime')  # Field name made lowercase.
    isnew = models.CharField(db_column='IsNew', max_length=1, blank=True, null=True)  # Field name made lowercase.
    islook = models.CharField(db_column='IsLook', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_msgpromotions'


class TSysMsgtype(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    sendway = models.CharField(db_column='SendWay', max_length=1, blank=True, null=True)  # Field name made lowercase.
    claasifyname = models.CharField(db_column='ClaasifyName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iconspath = models.CharField(db_column='IconsPath', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_msgtype'


class TSysMsgusersetup(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_msgtypeid = models.IntegerField(db_column='FK_MsgTypeID', blank=True, null=True)  # Field name made lowercase.
    fk_memberid = models.IntegerField(db_column='FK_MemberID', blank=True, null=True)  # Field name made lowercase.
    sign = models.CharField(db_column='Sign', max_length=1, blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='StartTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='EndTime', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_msgusersetup'


class TSysProvice(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=6, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_provice'


class TSysRole(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_departmentid = models.IntegerField(db_column='FK_DepartmentID', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=40, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_role'


class TSysRolepower(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_roleid = models.IntegerField(db_column='FK_RoleID', blank=True, null=True)  # Field name made lowercase.
    fk_menuid = models.IntegerField(db_column='FK_MenuID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_rolepower'


class TSysServiceinfo(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    servicecode = models.CharField(db_column='ServiceCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    servicename = models.CharField(db_column='ServiceName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    serviceurl = models.CharField(db_column='ServiceUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    classname = models.CharField(db_column='ClassName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    actionname = models.CharField(db_column='ActionName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    issign = models.CharField(db_column='IsSign', max_length=1, blank=True, null=True)  # Field name made lowercase.
    noparams = models.CharField(db_column='NoParams', max_length=200, blank=True, null=True)  # Field name made lowercase.
    servicecontent = models.CharField(db_column='ServiceContent', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime')  # Field name made lowercase.
    sign = models.CharField(db_column='Sign', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_serviceinfo'


class TSysUser(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_roleid = models.IntegerField(db_column='FK_RoleID', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=40, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PassWord', max_length=40, blank=True, null=True)  # Field name made lowercase.
    truename = models.CharField(db_column='TrueName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_user'


class TSysUserpower(models.Model):
   # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fk_userid = models.IntegerField(db_column='FK_UserID', blank=True, null=True)  # Field name made lowercase.
    fk_menuid = models.IntegerField(db_column='FK_MenuID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sys_userpower'


class TTag(models.Model):
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    tagcode = models.CharField(db_column='TagCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tagname = models.CharField(db_column='TagName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    productnumber = models.IntegerField(db_column='ProductNumber', blank=True, null=True)  # Field name made lowercase.
    sign = models.CharField(db_column='Sign', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ishot = models.CharField(db_column='IsHot', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_tag'
