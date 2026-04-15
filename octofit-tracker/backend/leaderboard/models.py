from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LeaderboardEntry(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)
    total_activities = models.IntegerField(default=0)
    total_duration = models.IntegerField(default=0)  # in minutes

    def __str__(self):
        return f"{self.user.username} - {self.total_points} points"
