#_*_encoding:utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile, Banner,UserMessage,MyServiceMan,MyOrder
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
        if login_form.is_valid():  #obj.is_valid方法，来检查用户输入的内容，跟Form（）定义的，是否匹配。
           user_name = request.POST.get("username", "")
           pass_word = request.POST.get("password", "")
           user = authenticate(username=user_name, password=pass_word)
           all_message=UserMessage.objects.filter(user=user)
           my_serviceman=MyServiceMan.objects.filter(user=user)
           my_order=MyOrder.objects.filter(user=user)
           if user is not None:
               login(request, user)
               return render(request, 'usercenter-info.html', {#登录成功
                  "user": user,
                  "all_message": all_message,
                  "my_serviceman":my_serviceman,
                  "my_order":my_order,
               })
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
            user=authenticate(username=user_name,password=pass_word)
            all_message = UserMessage.objects.filter(user=user)
            my_serviceman = MyServiceMan.objects.filter(user=user)
            my_order = MyOrder.objects.filter(user=user)
            if user is not None:
                login(request, user)
                return render(request,"usercenter-info.html",{
                    "user": user,
                    "all_message": all_message,
                    "my_serviceman": my_serviceman,
                    "my_order": my_order,

            })
        else:
            return render(request,"register.html",{
                "register_form":register_form,
                "msg":"请用邮箱注册"
            })

class LogoutView(View):
    """
    用户登出

    """
    def get(self,request):
        logout(request)
        from django.core.urlresolvers import reverse
        return HttpResponseRedirect(reverse("index"))





class UserinfoView(LoginRequiredMixin,View):
    """
    用户个人信息
    """

    def get(self, request):
        #个人消息

        all_message = UserMessage.objects.filter(user=request.user)
        my_serviceman=MyServiceMan.objects.filter(user=request.user)
        my_order=MyOrder.objects.filter(user=request.user)
        return render(request, 'usercenter-info.html',{
            "all_message": all_message,
            "my_serviceman":my_serviceman,
            "my_order":my_order,


        })





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