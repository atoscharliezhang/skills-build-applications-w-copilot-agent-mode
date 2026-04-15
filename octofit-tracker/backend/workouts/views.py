from django.shortcuts import render
from rest_framework import viewsets
from .models import WorkoutSuggestion
from .serializers import WorkoutSuggestionSerializer

# Create your views here.

class WorkoutSuggestionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSuggestion.objects.all()
    serializer_class = WorkoutSuggestionSerializer
