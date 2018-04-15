#_*_encoding:utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile, Banner
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm ,RegisterForm
from django.contrib.auth.hashers import make_password
from utils.mixin_utils import LoginRequiredMixin

# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user= UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class Cooperator(View):
    def get(self,request):
        return render(request,"cooperator-plan.html",{})


class CustomerView(View):
    def get(self,request):
        return render(request,"customer-service.html",{})



class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})
    def post(self,request):
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
           user_name = request.POST.get("username", "")
           pass_word = request.POST.get("password", "")
           user = authenticate(username=user_name, password=pass_word)
           if user is not None:
               login(request, user)
               return render(request, "usercenter-info.html")  #登录成功
           else:
               return render(request, "login.html",{"msg":"用户名或者密码错误！"})


        else:
            return render(request, "login.html", {"login_form":login_form})



class RegisterView(View):
    def get(self,request):
        register_form=RegisterForm()
        return render(request, "register.html", {'register_form':register_form})

    def post(self,request):
        register_form=RegisterForm(request.POST)
        if register_form.is_valid():
            user_name=request.POST.get("email","")
            pass_word=request.POST.get("password","")
            user_profile=UserProfile()
            user_profile.username=user_name
            user_profile.email=user_name
            user_profile.password=make_password(pass_word)
            user_profile.save()

            return render(request,"usercenter-info.html")
        else:
            return render(request,"register.html",{"register_form":register_form})


class UserinfoView(LoginRequiredMixin,View):
    """
    用户个人信息
    """

    def get(self, request):
        return render(request, 'usercenter-info.html',{


        })


class MymessageView(LoginRequiredMixin, View):
    """
    我的消息
    """
    def get(self, request):
        return render(request,'usercenter-message.html',{ })


class IndexView(View):
    #首页
    def get(self, request):

        #取出轮播图
       # all_banners=Banner.objects.all().order_by('index')
        # courses=Course.objects.filter(is_banner=False)[:5]
        # banner_courses=Course.objects.filter(is_banner=False)[:3]
        # course_orgs=CourseOrg.objects.all()[:6]
        return  render(request, 'index.html',{
          #  'all_banners':all_banners,
            # 'courses':courses,
            # 'banner_courses':banner_courses

        })


#
# # class Mingrenmingyan:
# #     """
# #     处理名人名言接口返回的数据
# #     """
# #     def __init__(self):
# #         """
# #         初始化相关数据,包括接口的url,headers和parm
# #         :return: None
# #         """
# #         self.url = 'http://api.lixing.biz/service?method=getUpdateProductInfo'
# #         self.headers = {"C100000362": "4a071cd838d7fbeec1225dd7d125be3a"}
# #         self.parm = {
# #             "dtype": "JSON",
# #             "keyword": "人生",
# #             "page": "1",
# #             "rows": "20"
#         }