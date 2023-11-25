# Generated by Django 4.2.7 on 2023-11-25 21:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_alter_jobdescription_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdescription',
            name='benefits',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='experience_year',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='gender',
            field=models.CharField(blank=True, choices=[('MALE', 'Nam'), ('FEMALE', 'Nữ'), ('BOTH', 'Cả hai'), ('UNKNOWN', 'Không yêu cầu')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='number_of_recruits',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='requirements',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='salary_end',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='salary_start',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='work_form',
            field=models.CharField(blank=True, choices=[('PART_TIME', 'Bán thời gian'), ('FULL_TIME', 'Toàn thời gian'), ('BOTH', 'Cả hai')], max_length=20, null=True),
        ),
    ]
