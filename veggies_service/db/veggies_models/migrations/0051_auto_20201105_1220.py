# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-05 06:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggies_models', '0050_auto_20201103_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='is_extra_paid_delivery',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='used_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'bd78ba13-8a51-40c4-8166-220131bfc899', max_length=128),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 5, 12, 25, 23, 435898)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='uuId',
            field=models.CharField(default=b'306b40b8-c277-47b2-9414-fad2bd29ef3c', max_length=512),
        ),
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default=b'd60bbae2-8325-441b-a393-fcf2b42c424f', max_length=1024),
        ),
    ]