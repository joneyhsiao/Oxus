# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('contact', models.CharField(default=11111111111, max_length=16)),
                ('email', models.CharField(default='someone@email.com', max_length=255)),
                ('role', models.CharField(choices=[(1, '管理员'), (2, '普通用户')], default=2, max_length=2)),
                ('age', models.IntegerField(default=3)),
                ('gender', models.BooleanField(default=False)),
                ('memo', models.TextField(default='Memo')),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
