from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Project

def project(request, project_shortname):
    current_project = get_object_or_404(Project, project_shortname__exact=project_shortname)
    return render(request, 'portfolio/project.html', {'current_project': current_project,})

def index(request):
    latest_project_list = Project.objects.all()
    context = {'latest_project_list': latest_project_list,}
    return render(request, 'portfolio/index.html', context)