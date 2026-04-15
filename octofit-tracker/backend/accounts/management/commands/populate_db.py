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
        ironman.save()
        captain = User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password')
        captain.save()
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')
        batman.save()
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password')
        superman.save()
        print('Users created')

        # Create Teams (created_by required)
        marvel = Team.objects.create(name='Team Marvel', description='Marvel superheroes', created_by=ironman)
        marvel.save()
        dc = Team.objects.create(name='Team DC', description='DC superheroes', created_by=batman)
        dc.save()
        marvel.members.set([ironman, captain])
        dc.members.set([batman, superman])
        marvel.save()
        dc.save()
        print('Teams created and members set')

        # Create Activities
        a1 = Activity.objects.create(user=ironman, activity_type='running', duration=30, distance=5)
        a1.save()
        a2 = Activity.objects.create(user=captain, activity_type='walking', duration=60, distance=4)
        a2.save()
        a3 = Activity.objects.create(user=batman, activity_type='strength_training', duration=45, distance=0)
        a3.save()
        a4 = Activity.objects.create(user=superman, activity_type='running', duration=50, distance=10)
        a4.save()
        print('Activities created')

        # Create Workouts
        w1 = WorkoutSuggestion.objects.create(user=ironman, title='Chest Day', description='Bench press and pushups', exercises=["Bench Press", "Pushups"], duration=40, difficulty='medium')
        w1.save()
        w2 = WorkoutSuggestion.objects.create(user=batman, title='Leg Day', description='Squats and lunges', exercises=["Squats", "Lunges"], duration=35, difficulty='hard')
        w2.save()
        print('Workouts created')

        # Create Leaderboard Entries
        l1 = LeaderboardEntry.objects.create(user=ironman, total_points=100, total_activities=5, total_duration=120)
        l1.save()
        l2 = LeaderboardEntry.objects.create(user=batman, total_points=120, total_activities=6, total_duration=150)
        l2.save()
        l3 = LeaderboardEntry.objects.create(user=superman, total_points=110, total_activities=4, total_duration=100)
        l3.save()
        l4 = LeaderboardEntry.objects.create(user=captain, total_points=90, total_activities=3, total_duration=80)
        l4.save()
        print('Leaderboard entries created')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
