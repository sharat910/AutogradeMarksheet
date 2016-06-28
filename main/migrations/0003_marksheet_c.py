# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_marksheet_t'),
    ]

    operations = [
        migrations.AddField(
            model_name='marksheet',
            name='c',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
    ]
