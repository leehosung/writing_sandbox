# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_phrase_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='description',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
