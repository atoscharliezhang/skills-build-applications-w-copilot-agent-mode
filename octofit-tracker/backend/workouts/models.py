from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class WorkoutSuggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    exercises = models.JSONField()  # list of exercises
    duration = models.IntegerField(help_text="Suggested duration in minutes")
    difficulty = models.CharField(max_length=50, choices=[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} for {self.user.username}"
