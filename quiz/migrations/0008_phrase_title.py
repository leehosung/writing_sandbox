# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_phrase_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='phrase',
            name='title',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
