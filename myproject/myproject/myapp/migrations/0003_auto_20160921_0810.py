# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20160921_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='%Y-%m'),
        ),
    ]