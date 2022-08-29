from django.urls import path

from . import views

app_name = 'portfoilo'
urlpatterns = [
    path('', views.index, name='index'),
    path('project/<str:project_shortname>/', views.project, name='project'),
]