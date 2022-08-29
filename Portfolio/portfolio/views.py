from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Project

def project(request, project_shortname):
    current_project = get_object_or_404(Project, project_shortname__exact=project_shortname)
    return render(request, 'portfolio/project.html', {'current_project': current_project,})

'''
def index(request):
    latest_project_list = Project.objects.all()
    context = {'latest_project_list': latest_project_list,}
    return render(request, 'portfolio/index.html', context)
'''

class IndexView(generic.ListView):
    template_name = 'portfolio/index.html'
    context_object_name = 'latest_project_list'

    def get_queryset(self):
        return Project.objects.all()

class ProjectView(generic.DetailView):
    model = Project
    template_name = 'portfolio/project.html'

    def get_object(self):
        self.project = get_object_or_404(Project, project_shortname__exact=self.kwargs['project_shortname'])
        return Project.objects.filter(id=self.project.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context
