# Generated by Django 4.2.7 on 2023-11-25 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_jobdescription_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdescription',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
    ]