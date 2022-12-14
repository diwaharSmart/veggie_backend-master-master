# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-21 13:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggies_models', '0037_auto_20201012_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default=b'd0317e7a-07f1-4c3c-a6e0-6dc55ccdfed9', max_length=1024),
        ),
        migrations.AddField(
            model_name='user',
            name='verification_sent_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'8e513ed8-7b3c-4d49-a3ee-17e2aaa9bde1', max_length=128),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 21, 19, 15, 26, 447103)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='uuId',
            field=models.CharField(default=b'4f7470f1-66dd-4436-ace1-b1e84beefcd7', max_length=512),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('GM', 'GM'), ('KG', 'KG'), ('ML', 'ML'), ('LTR', 'LTR'), ('PIECE', 'PIECE')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='quantities',
            name='unit',
            field=models.CharField(choices=[('GM', 'GM'), ('KG', 'KG'), ('ML', 'ML'), ('LTR', 'LTR'), ('PIECE', 'PIECE')], max_length=64),
        ),
    ]
