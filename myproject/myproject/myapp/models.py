# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
    # docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    # docfile = models.FileField(upload_to='doc-%Y-%m')
    CHOICE_STATUS = (
        ('安排面試','安排面試'),
        ('面試不通過','面試不通過'),
        ('面試通過','面試通過'),
    )
    
    f01 = models.CharField(default=".",max_length=99,verbose_name="編號")
    f02 = models.CharField(default=".",max_length=99,verbose_name="姓名")
    f03 = models.CharField(default=".",max_length=99,verbose_name="應徵職務")
    f05 = models.CharField(default=".",max_length=99,verbose_name="備註")
    # f05 = models.CharField(default=".",max_length=99,verbose_name="應徵職務")
    docfile = models.FileField(upload_to='%Y-%m' ,verbose_name="簡歷檔案")
    f04 = models.CharField(default="安排面試",max_length=99,verbose_name="面試記錄", choices=CHOICE_STATUS)
 
    
    def __str__(self):
        return self.f01+" "+self.f02+" "+self.f03+" "+self.f04+" "+self.f05+" "
