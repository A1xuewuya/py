from django.db import models
from tinymce.models import HTMLField


class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=32)
    isDelete = models.BooleanField(default=False)


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=32)
    gpic = models.ImageField(upload_to='df_goods')
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    gunit = models.CharField(max_length=16)
    gclick = models.IntegerField()
    gjianjie = models.CharField(max_length=200)
    gkucun = models.IntegerField()
    gcount = HTMLField()
    gtype = models.ForeignKey('TypeInfo')
    gadv = models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)
