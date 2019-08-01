from django.shortcuts import render,redirect
import datetime as dt
from .models import Projects
from django.contrib.auth.decorators import login_required
from .forms import ProjectsForm

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

@login_required(login_url='/accounts/login')
def upload_projects(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            upload=form.save(commit=False)
            upload.profile = request.user.profile
            upload.save()
            return redirect('index')
    else:
        form = ProjectsForm()
    return render(request,'update_projects.html',{'form':form})

@login_required(login_url='/accounts/login')
def search_projects(request):
    if 'projects' in request.GET and request.GET["projects"]:
        search_term=request.GET.get("projects")
        searched_projects=Projects.search_by_title(search_term)
        message=f"{search_term}"
        return render(request,'search.html',{"message":message,"projects":searched_projects})
