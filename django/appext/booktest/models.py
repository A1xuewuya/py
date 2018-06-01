from django.db import models


class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    prea = models.ForeignKey('self', null=True, blank=True)
