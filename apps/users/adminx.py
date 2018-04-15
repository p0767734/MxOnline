#_*_coding:utf-8 _*_

_author_ = 'bobby'
_date_ = '2017/11/20 21:07'

import xadmin
from .models import Banner, UserProfile,UserMessage, MyServiceMan, MyOrder

class BannerAdmin(object):

    list_display=['title','image','url','index','add_time']
    search_fields=['title','image','url','index']
    list_filter=['title','image','url','index','add_time']





class UserProfileAdmin(object):

    list_display = ['user_name', 'gender', 'mobile']
    search_fields = ['user_name', 'gender', 'mobile']
    list_filter = ['user_name', 'gender', 'mobile']



class UserMessageAdmin(object):

    list_display = ['user', 'message','add_time']
    search_fields = ['user', 'message']
    list_filter = ['user', 'message','add_time']




class MyServiceManAdmin(object):
    list_display = ['user', 'serviceman', 'add_time']
    search_fields = ['user', 'serviceman']
    list_filter = ['user', 'serviceman', 'add_time']



class MyOrderAdmin(object):
    list_display = ['user', 'order', 'add_time']
    search_fields = ['user', 'order']
    list_filter = ['user', 'order', 'add_time']

xadmin.site.register(Banner,BannerAdmin)
#xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)

xadmin.site.register(MyServiceMan, MyServiceManAdmin)
xadmin.site.register(MyOrder, MyOrderAdmin)
