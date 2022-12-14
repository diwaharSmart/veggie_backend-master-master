# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-05 18:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veggies_models', '0026_auto_20201003_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('BASKET', 'BASKET'), ('NORMAL', 'NORMAL')], default='NORMAL', max_length=64),
        ),
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'e5614572-9f18-465f-bb12-6fe036571882', max_length=128),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 6, 0, 1, 20, 996523)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='uuId',
            field=models.CharField(default=b'5f5119cd-ba6e-4553-b0d0-1ef65fd9c54d', max_length=512),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='veggies_models.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='mrp',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
