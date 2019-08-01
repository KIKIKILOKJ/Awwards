from django.shortcuts import render
import datetime as dt
from .models import Projects
from django.contrib.auth.decorators import login_required

# Create your views here.
def convert_dates(dates):
    # function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','thursday','Friday','Saturday','Sunday']
    '''
    Returns the actual day of the week
    '''
    day = days[day_number]
    return day

def index(request):
    date=dt.date.today
    projects=Projects.objects.all()
    return render(request,'index.html',{"date": date, "projects": projects})

@login_required(login_url='/accounts/login')
def projects(request,id):
    projects= Projects.objects.filter(id__icontains = id)
    return render(request,"projects.html",{"projects": projects})
