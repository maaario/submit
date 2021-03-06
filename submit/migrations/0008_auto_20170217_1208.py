# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-17 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0007_auto_20170216_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='submitreceiver',
            name='token',
            field=models.CharField(help_text='Secret key allowing external submits via API, will be generated automatically.', max_length=64, unique=True, verbose_name=b'token'),
        ),
    ]
