from django.shortcuts import render
from .models import User, Project

def all_projects(request):
    project_list = Project.objects.all()
    return render(request, 'projects/projects.html', {'project_list': project_list})
# Create your views here.
