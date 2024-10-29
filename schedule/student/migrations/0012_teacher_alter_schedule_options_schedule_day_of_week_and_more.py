# Generated by Django 5.1.2 on 2024-10-29 02:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_remove_subject_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'verbose_name': 'Расписание', 'verbose_name_plural': 'Расписания'},
        ),
        migrations.AddField(
            model_name='schedule',
            name='day_of_week',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], default=1, max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.TimeField(verbose_name='Время начала занятий'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.teacher'),
            preserve_default=False,
        ),
    ]
