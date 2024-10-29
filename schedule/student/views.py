
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return HttpResponse("Home page")



def day(request, day):
    print(f"day = {day}")

    if day == 'week':
        schedule = Schedule.objects.all()

        return render(request,
                      template_name="Home.html",
                      context={"data": schedule})
    return HttpResponse("ERROR")
