from django.shortcuts import render
from .models import User, Project
from .forms import ProjectForm
from django.http import HttpResponseRedirect

def all_projects(request):
    project_list = Project.objects.all()
    return render(request, 'projects/projects.html', {'project_list': project_list})

def add_projects(request):
    submitted = False
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-projects?submitted=True')
    else:
        form = ProjectForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'projects/add_projects.html', {'form':form, 'submitted':submitted})
# Create your views here.
