# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
    # docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    # docfile = models.FileField(upload_to='doc-%Y-%m')
    docfile = models.FileField(upload_to='%Y-%m')
    
