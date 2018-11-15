# Generated by Django 2.0 on 2018-11-15 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watermarking', '0030_watermarking_extract_code'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='metricnoisesprintwatermarking',
            unique_together={('metric', 'noiseSprintWatermarking')},
        ),
        migrations.AlterUniqueTogether(
            name='metricsprintwatermarking',
            unique_together={('metric', 'sprintWatermarking')},
        ),
        migrations.AlterUniqueTogether(
            name='noisesprintwatermarking',
            unique_together={('noise', 'sprintWatermarking')},
        ),
        migrations.AlterUniqueTogether(
            name='sprintwatermarking',
            unique_together={('watermarking', 'cover_image', 'watermark')},
        ),
    ]
