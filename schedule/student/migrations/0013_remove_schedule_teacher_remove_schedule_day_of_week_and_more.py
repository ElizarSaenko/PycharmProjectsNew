# Generated by Django 5.1.2 on 2024-10-29 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_teacher_alter_schedule_options_schedule_day_of_week_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='day_of_week',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.TimeField(help_text='Среда не рабочий день', verbose_name='Время начала занятий'),
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]