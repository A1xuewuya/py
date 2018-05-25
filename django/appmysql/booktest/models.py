from django.db import models


class BookInfo(models.Model):
    btitle = models.CharField(max_length=32)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey(BookInfo)
    isDelete = models.BooleanField(default=False)
