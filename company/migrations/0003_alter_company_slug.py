# Generated by Django 4.2.7 on 2023-11-25 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
    ]