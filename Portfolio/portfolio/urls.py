from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /project/5/
    path('<int:project_id>/', views.detail, name='detail'),
    # ex: /project/projname/
    path('project/<str:project_shortname>/', views.project, name='project'),
]