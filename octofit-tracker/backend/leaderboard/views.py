from django.shortcuts import render
from rest_framework import viewsets
from .models import LeaderboardEntry
from .serializers import LeaderboardEntrySerializer

# Create your views here.

class LeaderboardEntryViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.all().order_by('-total_points')
    serializer_class = LeaderboardEntrySerializer
