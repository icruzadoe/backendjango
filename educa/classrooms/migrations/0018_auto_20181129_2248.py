# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0017_auto_20181128_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='text',
            old_name='content',
            new_name='text',
        ),
    ]
