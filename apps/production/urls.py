#_*_coding:utf-8 _*_

_author_ = 'bobby'


from django.conf.urls import url, include

from .views import ProductListView,IndexProductListView



urlpatterns = [


             #产品列表页


            #讲师详情页
            # url(r'^product/detail/(?P<product_id>\d+)/$', TeacherDetailView.as_view(), name="teacher_detail"),



        ]
