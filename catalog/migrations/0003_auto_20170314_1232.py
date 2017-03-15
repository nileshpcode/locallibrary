# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_extendedflatpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendedflatpage',
            name='page_type',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='extendedflatpage',
            name='image',
            field=models.FileField(upload_to='flatpage/media/'),
        ),
    ]