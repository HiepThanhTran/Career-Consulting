# Generated by Django 4.2.7 on 2023-11-16 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='full_name',
        ),
    ]
