from django.db import models


class Hostage(models.Model):
    name = models.fields.CharField(max_length=225)
    pray_name = models.fields.CharField(default='',max_length=225)
    info = models.fields.CharField(max_length=2010)
    english_name = models.fields.CharField(default='',max_length=225)
    english_info = models.fields.CharField(default='',max_length=2010)
    img = models.fields.CharField(max_length=2010)
    url = models.fields.CharField(max_length=2010)
