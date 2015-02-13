# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_sentence'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentence',
            name='article',
            field=models.ForeignKey(to='quiz.Article', default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sentence',
            name='language',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sentence',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sentence',
            name='sentence',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
