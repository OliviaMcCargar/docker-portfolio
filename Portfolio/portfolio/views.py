from pickle import TRUE
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Project, Job, Responsibility

class IndexView(generic.ListView):
    template_name = 'portfolio/index.html'
    context_object_name = 'latest_project_list'

    def get_queryset(self):
        return Project.objects.all().order_by("display_order")
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['jobs'] = Job.objects.filter(projects_only = False).order_by("display_order")
        context['current_jobs'] = Job.objects.filter(current_job=True)
        context['current_jobs'] = context['current_jobs'].filter(projects_only=False)
        context['responsibilities'] = Responsibility.objects.all()
        context['spc_responsibilities'] = Responsibility.objects.filter(job__id=1)
        context['apc_responsibilities'] = Responsibility.objects.filter(job__id=2)
        context['da_responsibilities'] = Responsibility.objects.filter(job__id=3)
        return context

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
