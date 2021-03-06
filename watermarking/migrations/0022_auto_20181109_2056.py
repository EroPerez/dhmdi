# Generated by Django 2.0 on 2018-11-10 01:56

import django.core.validators
from django.db import migrations, models
import watermarking.models


class Migration(migrations.Migration):

    dependencies = [
        ('watermarking', '0021_auto_20181109_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='source_code',
            field=models.FileField(upload_to=watermarking.models.random_metric_code_name, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['py'], message="Please upload '.py' files only.")]),
        ),
    ]
