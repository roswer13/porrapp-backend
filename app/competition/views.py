from rest_framework import generics, authentication, permissions
from django.shortcuts import render

from competition.serializer import CompetitionSerializer, TeamSerializer, MatchSerializer
from core.models import Competition, Team, Match


class CompetitionListView(generics.ListAPIView):
    queryset = Competition.objects.all().order_by('id')
    serializer_class = CompetitionSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class TeamListView(generics.ListAPIView):
    queryset = Team.objects.all().order_by('id')
    serializer_class = TeamSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class MatchListView(generics.ListAPIView):
    queryset = Match.objects.all().order_by('id')
    serializer_class = MatchSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]