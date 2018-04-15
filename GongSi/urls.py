#_*_encoding:utf-8_*_
"""GongSi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

import xadmin
from django.views.static import serve

from users.views import LoginView, RegisterView
from production.views import ProductListView,IndexView
from GongSi.settings import MEDIA_ROOT
from production.views import ProductDetailView
from users.views import UserinfoView ,MymessageView,Cooperator,CustomerView


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url('^$', IndexView.as_view(), name="index"),
   # url('^login/$', LoginView.as_view(),name="login"),

   # url('^$', IndexProductListView.as_view(),name="index"),

    url(r'^product/list/$', ProductListView.as_view(), name="product_list"),

    #图片上传路径
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),


    #合伙人详情页
    url('^cooperator/$',Cooperator.as_view(),name="cooperator"),

    #联系客服页
    url('^customer/$', CustomerView.as_view(), name="customer"),

    #产品详情页
    url(r'^product/detail/(?P<product_id>\d+)/$', ProductDetailView.as_view(), name="product_detail"),

    url('^login/$', LoginView.as_view(), name="login"),

    url('^register/$', RegisterView.as_view(), name="register"),

    #验证码
    url(r'^captcha/', include('captcha.urls')),

    # 用户信息
    url(r'^info/$', UserinfoView.as_view(), name="user_info"),

    # 我的消息
    url(r'^mymessage/$', MymessageView.as_view(), name="mymessage"),


    #个人中心
    url(r'^info/$', UserinfoView.as_view(), name="user_info"),

    #富文本编辑
    url(r'^ueditor/',include('DjangoUeditor.urls' )),


]
