from django.db import models


class BookInfo(models.Model):
    btitle = models.CharField(max_length=32)
    bpub_date = models.DateTimeField(db_column='bpub_date')
    bread = models.IntegerField()
    bcomment = models.IntegerField()
    isDelete = models.BooleanField()

    # class Meta():
    #     db_table = ''


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    isDelete = models.BooleanField()
    book = models.ForeignKey('BookInfo')

    def showContent(self):
        return self.hcontent
