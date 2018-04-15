#_*_encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class Production(models.Model):
    name=models.CharField(max_length=50, verbose_name=u"产品名称")
    desc=models.CharField(max_length=300, verbose_name=u"业务描述")
    # detail=UEditorField(verbose_name=u"内容",width=600, height=300, imagePath="production/ueditor/",
    #                                      filePath="production/ueditor/", default='', toolbars='full')
    detail = UEditorField(max_length=200, verbose_name=u"内容")
    degree=models.CharField(choices=(("lw","劳务"),("cw","财务")), max_length=4)
    max_price=models.FloatField(max_length=10,verbose_name=u"最高价格")
    min_price=models.FloatField(max_length=10, verbose_name=u"最低价格")
    image=models.ImageField(upload_to="productionimage/%Y/%m",verbose_name=u"产品封面图", max_length=1000)
    index=models.IntegerField(default=100, verbose_name=u"产品排序")
    add_time=models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")



    class Meta:
        verbose_name=u"产品服务"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name

class CustomerComments(models.Model):
    "业务评论"
    user=models.CharField(max_length=50, verbose_name=u"客户")
    product=models.ForeignKey(Production,verbose_name=u"产品名称")
    comments=UEditorField(verbose_name=u"评论内容",width=600, height=300, imagePath="production/ueditor/",
                                         filePath="production/ueditor/", default='', toolbars='full')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"客户评论"
        verbose_name_plural=verbose_name
