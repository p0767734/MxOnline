#_*_coding:utf-8 _*_

_author_ = 'bobby'
_date_ = '2017/11/20 21:07'

from django.conf.urls import url, include
from .views import UserinfoView



urlpatterns = [
    # 用户信息
    url(r'^info/$', UserinfoView.as_view(), name="user_info"),

    #课程评论


    #我的消息
    # url(r'^mymessage/$', UploadImageView.as_view(), name="mymessage")

               ]
