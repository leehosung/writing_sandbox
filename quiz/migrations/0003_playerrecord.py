# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20141105_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(default='')),
                ('phrase', models.ForeignKey(to='quiz.Phrase')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
