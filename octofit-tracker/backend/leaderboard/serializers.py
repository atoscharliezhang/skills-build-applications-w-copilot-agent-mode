from rest_framework import serializers
from .models import LeaderboardEntry

class LeaderboardEntrySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = LeaderboardEntry
        fields = ['user', 'total_points', 'total_activities', 'total_duration']