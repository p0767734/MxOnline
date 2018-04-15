#_*_coding:utf-8 _*_

_author_ = 'bobby'
_date_ = '2017/11/20 21:07'

import xadmin
from .models import  Production,CustomerComments

class ProductionAdmin(object):

    list_display=['name','desc','detail','degree','max_price','min_price','image','index','add_time']
    search_fields=['name','desc','detail','degree','max_price','min_price','image','index']
    list_filter=['name','desc','detail','degree','max_price','min_price','image','index','add_time']
    style_fields = {'detail':'ueditor'}



class CustomerCommentsAdmin(object):
    list_display=['user','product','comments','add_time']
    search_fields=['user','product','comments']
    list_filter=['user','product','comments','add_time']

xadmin.site.register(Production, ProductionAdmin)
xadmin.site.register(CustomerComments, CustomerCommentsAdmin)