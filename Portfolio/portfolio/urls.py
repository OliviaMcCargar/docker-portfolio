from django.urls import path

from . import views

app_name = 'portfoilo'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('project/twitterpubhealth/', views.TwitterPubHealthView.as_view(), name='twitterpubhealth'),
    path('project/<str:project_shortname>/', views.ProjectView.as_view(), name='project'),
]