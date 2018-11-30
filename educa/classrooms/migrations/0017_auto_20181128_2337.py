# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classrooms', '0016_auto_20180713_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=1000)),
                ('author', models.ForeignKey(related_name='text_wrote', to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(related_name='texts_created', to='classrooms.CourseInClassroom')),
                ('readers', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.RemoveField(
            model_name='studentincourse',
            name='final',
        ),
        migrations.RemoveField(
            model_name='studentincourse',
            name='midterm',
        ),
        migrations.RemoveField(
            model_name='studentincourse',
            name='pc4',
        ),
    ]
