
from django.contrib import admin
from django.urls import path
from .views import TeamViewById, TeamsViews

urlpatterns = [
    path('teams/', TeamsViews.as_view()), 
    path('teams/<team_id>/', TeamViewById.as_view()),  
  
]
