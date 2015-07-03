# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word_id', models.CharField(max_length=11)),
                ('verse_id', models.CharField(max_length=6)),
                ('paragraph_id', models.CharField(max_length=5)),
                ('sentence_id', models.CharField(max_length=6)),
                ('pos', models.CharField(max_length=2)),
                ('parse', models.CharField(max_length=8)),
                ('crit_text', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=50)),
                ('word', models.CharField(max_length=50)),
                ('norm', models.CharField(max_length=50)),
                ('lemma', models.CharField(max_length=50)),
                ('dep_type', models.CharField(max_length=4)),
                ('head', models.CharField(max_length=11, null=True)),
            ],
        ),
    ]
