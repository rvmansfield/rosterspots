from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teams', views.teams, name='teams'),
    path('teams/<slug:slug>', views.teamdetail, name='teamdetail'),
    path('addteam',views.addTeam, name='addteam')
]