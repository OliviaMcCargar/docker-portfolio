from django.urls import path

from . import views

app_name = 'portfoilo'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('project/twitterpubhealth/', views.TwitterPubHealthView.as_view(), name='twitterpubhealth'),
    path('project/stagesourcecensus/', views.StageSourceCensusView.as_view(), name='stagesourcecensus'),
    path('project/transpop/', views.TransPopView.as_view(), name='transpop'),
    path('project/<str:project_shortname>/', views.ProjectView.as_view(), name='project'),
]