# Generated by Django 4.2.7 on 2023-11-19 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.BooleanField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], null=True),
        ),
    ]