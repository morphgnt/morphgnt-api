# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('morphgnt_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['sblgnt_id']},
        ),
        migrations.AlterModelOptions(
            name='paragraph',
            options={'ordering': ['paragraph_id']},
        ),
        migrations.AlterModelOptions(
            name='sentence',
            options={'ordering': ['sentence_id']},
        ),
        migrations.AlterModelOptions(
            name='verse',
            options={'ordering': ['verse_id']},
        ),
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ['word_id']},
        ),
        migrations.AlterField(
            model_name='book',
            name='book_osis_id',
            field=models.CharField(max_length=6, db_index=True),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='book_osis_id',
            field=models.CharField(max_length=6, db_index=True),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='paragraph_id',
            field=models.CharField(max_length=5, db_index=True),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='book_osis_id',
            field=models.CharField(max_length=6, db_index=True),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='sentence_id',
            field=models.CharField(max_length=6, db_index=True),
        ),
        migrations.AlterField(
            model_name='verse',
            name='book_osis_id',
            field=models.CharField(max_length=6, db_index=True),
        ),
        migrations.AlterField(
            model_name='verse',
            name='verse_id',
            field=models.CharField(max_length=6, db_index=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='paragraph_id',
            field=models.CharField(max_length=5, db_index=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='sentence_id',
            field=models.CharField(max_length=6, db_index=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='verse_id',
            field=models.CharField(max_length=6, db_index=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='word_id',
            field=models.CharField(max_length=11, db_index=True),
        ),
    ]
