"""
URL mappings for the user API.
"""
from django.urls import path

from competition import views


app_name = 'competition'

urlpatterns = [
    path('competition', views.CompetitionListView.as_view(), name='competition-list'),
    path('teams', views.TeamListView.as_view(), name='team-list'),
    path('matches', views.MatchListView.as_view(), name='match-list'),
]
