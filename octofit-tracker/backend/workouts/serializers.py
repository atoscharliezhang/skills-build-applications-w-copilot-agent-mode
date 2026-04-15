from rest_framework import serializers
from .models import WorkoutSuggestion

class WorkoutSuggestionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = WorkoutSuggestion
        fields = ['id', 'user', 'title', 'description', 'exercises', 'duration', 'difficulty', 'created_at']