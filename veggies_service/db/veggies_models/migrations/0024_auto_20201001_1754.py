# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-01 17:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggies_models', '0023_auto_20201001_0726'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='used_points',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'fc605c0a-f254-4aa7-a882-60ebba12b537', max_length=128),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 1, 17, 59, 11, 106923)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='uuId',
            field=models.CharField(default=b'08f18a82-1862-4b6a-9a8e-ef86a8c61941', max_length=512),
        ),
    ]
