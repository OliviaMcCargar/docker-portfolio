from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Project

def detail(request, project_id):
    return HttpResponse("You're looking at project %s." % project_id)

def results(request, project_id):
    response = "You're looking at the description of project %s."
    return HttpResponse(response % project_id)

def index(request):
    latest_project_list = Project.objects.all()
    context = {'latest_project_list': latest_project_list,}
    return render(request, 'portfolio/index.html', context)