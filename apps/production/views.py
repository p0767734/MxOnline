#_*_encoding:utf-8_*_
from django.shortcuts import render
from django.views.generic import View
from .models import Production,CustomerComments
from users.models import Banner
from django.db.models import Q
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class ProductListView(View):
    """
    产品列表页
    """
    def get(self, request):
        all_Products = Production.objects.all()

        current_nav="Product"

        return render(request,"product_list.html",{
            "all_Products":all_Products,

            "current_nav":current_nav
        })


class IndexView(View):
    def get(self,request):
        all_Products=Production.objects.all()
        all_banners=Banner.objects.all().order_by('index')
        return render(request,"index.html",{
            'all_Products':all_Products,
            'all_banners':all_banners,
        })


class ProductDetailView(View):
    def get(self, request, product_id):
        product=Production.objects.get(id=int(product_id))
        all_comments=CustomerComments.objects.all()
        return render(request, "product_detail.html",{
            "product":product,
            "all_comments":all_comments,

        })

