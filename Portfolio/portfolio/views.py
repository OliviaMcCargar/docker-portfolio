from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Project

def detail(request, project_id):
    return HttpResponse("You're looking at project %s." % project_id)

def project(request, project_shortname):
    current_project = Project.objects.get(project_shortname__exact=project_shortname)
    context = {'current_project': current_project,}
    return render(request, 'portfolio/project.html', context)

def index(request):
    latest_project_list = Project.objects.all()
    context = {'latest_project_list': latest_project_list,}
    return render(request, 'portfolio/index.html', context)