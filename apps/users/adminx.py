#_*_coding:utf-8 _*_

_author_ = 'bobby'
_date_ = '2017/11/20 21:07'

import xadmin
from .models import Banner, UserProfile

class BannerAdmin(object):

    list_display=['title','image','url','index','add_time']
    search_fields=['title','image','url','index']
    list_filter=['title','image','url','index','add_time']





class UserProfileAdmin(object):

    list_display = ['user_name', 'gender', 'mobile']
    search_fields = ['user_name', 'gender', 'mobile']
    list_filter = ['user_name', 'gender', 'mobile']

xadmin.site.register(Banner,BannerAdmin)
#xadmin.site.register(UserProfile,UserProfileAdmin)
