from django.contrib import admin

# Register your models here.
from .models import Company, Department, Job, Responsibility, Project

admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Job)
admin.site.register(Responsibility)
admin.site.register(Project)
