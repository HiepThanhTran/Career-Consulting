# Generated by Django 4.2.7 on 2023-11-16 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_managers_alter_user_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_date',
        ),
    ]
