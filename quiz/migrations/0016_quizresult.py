# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0015_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typed_by_user', models.TextField(default=b'')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('sentence', models.ForeignKey(default=None, to='quiz.Sentence')),
                ('user', models.ForeignKey(default=None, to='quiz.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
