# Generated by Django 5.1.2 on 2024-10-16 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_schedule_start_time_remove_schedule_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='start_time',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='subject',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]