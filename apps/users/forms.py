#_*_coding:utf-8 _*_

_author_ = 'bobby'
_date_ = '2017/11/20 21:07'

from django import forms


from .models import UserProfile
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password=forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email=forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    #captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


# class UploadImageForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['image']


