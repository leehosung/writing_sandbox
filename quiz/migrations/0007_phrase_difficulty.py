# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20141116_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='phrase',
            name='difficulty',
            field=models.PositiveSmallIntegerField(default=32767),
            preserve_default=True,
        ),
    ]
