from django.db import models
from django.utils.translation import gettext_lazy as _
#['math', 'RUS', 'physics']

class Subject(models.Model):
    name = models.CharField(max_length=20)

class Schedule(models.Model): #название класса - название таблицы, которая будет создана
    class Meta:
        verbose_name = _('Расписание')
        verbose_name_plural = _('Расписания')
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE
    ) #ключ
    start_time = models.TimeField(verbose_name='Время начала занятий', help_text='Среда не рабочий день') #



