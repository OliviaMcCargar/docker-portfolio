from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=500)
    def __str__(self):
        return self.company_name

class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=500)
    def __str__(self):
        return self.department_name

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    current_job = models.BooleanField()
    def __str__(self):
        return self.job_name
    

class Responsibility(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    responsibility_name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    def __str__(self):
        return self.responsibility_name

class Project(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    outcome = models.CharField(max_length=2000)
    timeline = models.CharField(max_length=200)
    link = models.URLField()
    def __str__(self):
        return self.project_name