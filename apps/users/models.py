#_*_encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    user_name=models.CharField(max_length=50, verbose_name=u"客户姓名", default="")
    gender=models.CharField(max_length=6,choices=(("male",u"男"),("female","女")),default="male")
    mobile=models.CharField(max_length=15, null=True, blank=True)


    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.username

class Banner(models.Model):
    title=models.CharField(max_length=100, verbose_name=u"标题")
    image=models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    url=models.URLField(default="",max_length=200, blank=True,verbose_name=u"访问地址")
    index=models.IntegerField(default=100, verbose_name=u"顺序")
    add_time=models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"轮播图"
        verbose_name_plural=verbose_name



