# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_set_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('url', models.TextField(default='')),
                ('title', models.TextField(default='')),
                ('tags', models.TextField(default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
