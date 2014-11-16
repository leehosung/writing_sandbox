# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20141111_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phrase',
            name='set',
            field=models.ForeignKey(to='quiz.Set'),
            preserve_default=True,
        ),
    ]
