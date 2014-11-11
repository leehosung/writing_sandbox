# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_set'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phrase',
            old_name='category',
            new_name='set',
        ),
    ]
