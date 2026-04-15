from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'members', 'created_by', 'created_at']