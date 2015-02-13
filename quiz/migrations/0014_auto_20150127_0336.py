# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_hint'),
    ]

    operations = [
        migrations.AddField(
            model_name='hint',
            name='hint',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hint',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hint',
            name='sentence',
            field=models.ForeignKey(default=None, to='quiz.Sentence'),
            preserve_default=True,
        ),
    ]
