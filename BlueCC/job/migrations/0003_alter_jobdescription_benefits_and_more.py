# Generated by Django 4.2.7 on 2023-11-16 08:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdescription',
            name='benefits',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='requirements',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
