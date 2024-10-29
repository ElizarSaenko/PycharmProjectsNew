from django.contrib import admin
from .models import *

@admin.register(Schedule) #Это стандартная тема для создания  админа
class ScheduleAdmin(admin.ModelAdmin):
    pass

@admin.register(Subject) #Это стандартная тема для создания  админа
class SubjectAdmin(admin.ModelAdmin):
    pass