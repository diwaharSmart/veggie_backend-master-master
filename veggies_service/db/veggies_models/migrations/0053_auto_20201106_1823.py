# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-06 12:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggies_models', '0052_auto_20201106_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='location',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'4e2c10e9-85a8-46c6-b39c-619a79e4a282', max_length=128),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 6, 18, 28, 23, 692301)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='uuId',
            field=models.CharField(default=b'd4e4e3f2-b29a-4baf-92bb-fa99feee13a8', max_length=512),
        ),
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default=b'aea9c370-06b0-41d6-aac5-9dc31f6bb4b0', max_length=1024),
        ),
    ]
