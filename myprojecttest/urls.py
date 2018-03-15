"""myprojecttest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from apptest import views,Login,user,upload,product
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #url(r'^$', views.home),
    url(r'^login$', user.login),
    url(r'^login/loginSubmit$', user.register,name="loginSubmit"),
    url('^admin/', admin.site.urls),
   # url(r'^adddb$', views.adddb),
    #url(r'^selectdb$', views.selectdb),
    #url(r'^updatedb$', views.updatedb),
    #url(r'^deletedb$', views.deletedb),
    #url(r'^search$', views.search),
    url(r'^register$', user.register),
    url(r'^upload_avatar/', upload.upload_avatar,name="upload"), # 上传头像
    url(r'^test/', upload.test), # 测试页面
    url(r'^getuserinfo$', user.getuserinfo), # 用户信息
    url(r'^getmessage$', user.getmessagecode), # 获取短信验证码
    url(r'^checkmessage$', user.checkmessagecode), # 校验短信验证码
    url(r'^getmemcache$', user.getmemcache),
    url(r'^getfirstpage', product.getfirstpage),
    url(r'^searchproduct', product.searchproduct),
    url(r'^productdetail', product.productdetail),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)