# Generated by Django 5.1.2 on 2024-10-16 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_schedule_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='subject',
        ),
    ]
