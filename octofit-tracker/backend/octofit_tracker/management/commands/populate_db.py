
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from teams.models import Team
from activities.models import Activity
from leaderboard.models import LeaderboardEntry
from workouts.models import WorkoutSuggestion

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Team.objects.all().delete()
        WorkoutSuggestion.objects.all().delete()
        User.objects.exclude(is_superuser=True).delete()

        # Create Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
        captain = User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password')

        # Create Teams (created_by required)
        marvel = Team.objects.create(name='Team Marvel', description='Marvel superheroes', created_by=ironman)
        dc = Team.objects.create(name='Team DC', description='DC superheroes', created_by=batman)
        marvel.members.set([ironman, captain])
        dc.members.set([batman, superman])

        # Create Activities
        Activity.objects.create(user=ironman, activity_type='running', duration=30, distance=5)
        Activity.objects.create(user=captain, activity_type='walking', duration=60, distance=4)
        Activity.objects.create(user=batman, activity_type='strength_training', duration=45, distance=0)
        Activity.objects.create(user=superman, activity_type='running', duration=50, distance=10)

        # Create Workouts
        WorkoutSuggestion.objects.create(user=ironman, title='Chest Day', description='Bench press and pushups', exercises=["Bench Press", "Pushups"], duration=40, difficulty='medium')
        WorkoutSuggestion.objects.create(user=batman, title='Leg Day', description='Squats and lunges', exercises=["Squats", "Lunges"], duration=35, difficulty='hard')

        # Create Leaderboard Entries
        LeaderboardEntry.objects.create(user=ironman, total_points=100, total_activities=5, total_duration=120)
        LeaderboardEntry.objects.create(user=batman, total_points=120, total_activities=6, total_duration=150)
        LeaderboardEntry.objects.create(user=superman, total_points=110, total_activities=4, total_duration=100)
        LeaderboardEntry.objects.create(user=captain, total_points=90, total_activities=3, total_duration=80)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
