# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-16 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0006_auto_20170216_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitreceiver',
            name='allow_external_submits',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submitreceiver',
            name='token',
            field=models.CharField(default=b'', help_text='Secret key allowing external submits via API, will be generated when allow_external_submits is checked.', max_length=64, verbose_name=b'token'),
        ),
    ]
