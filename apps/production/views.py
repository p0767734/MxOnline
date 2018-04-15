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

class FinanceView(View):
    def get(self,request):
        return render(request,"finance_service.html",{})


class Company_registerView(View):
    def get(self,request):
        return render(request, "company_register.html")


class CopyrightView(View):
    def get(self,request):
        return render(request, "copyright_service.html")

class Human_resourceView(View):
    def get(self, request):
        return render(request,"human_resource.html")

class Oversea_businesseView(View):
    def get(self,request):
        return render(request, "oversea_business.html")


class Add_valueView(View):
    def get(self,request):
        return render(request, "add_value.html")

class Audit_serviceView(View):
    def get(self,request):
        return render(request, "audit_service.html")





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
        relate_courses = CustomerComments.objects.filter(id__in=product_id)
        return render(request, "product_detail.html",{
            "product":product,
            "relate_courses":relate_courses,
        })

