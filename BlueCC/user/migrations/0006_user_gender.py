# Generated by Django 4.2.7 on 2023-11-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]