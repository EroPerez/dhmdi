# Generated by Django 2.0 on 2018-11-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watermarking', '0025_auto_20181110_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='metric',
            name='metric_type',
            field=models.CharField(choices=[('1', 'Watermarked'), ('2', 'Watermark')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
