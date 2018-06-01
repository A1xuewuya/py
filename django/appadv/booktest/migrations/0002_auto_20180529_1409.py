# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('btitle', models.CharField(max_length=32)),
                ('bpub_date', models.DateTimeField(db_column=b'bpub_date')),
                ('bread', models.IntegerField()),
                ('bcomment', models.IntegerField()),
                ('isDelete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField()),
                ('hcontent', models.CharField(max_length=100)),
                ('isDelete', models.BooleanField()),
                ('book', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
