from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Captain America', email='cap@marvel.com', team=marvel),
            User(name='Batman', email='batman@dc.com', team=dc),
            User(name='Superman', email='superman@dc.com', team=dc),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create activities
        activities = [
            Activity(user=users[0], type='Running', duration=30, calories=300, date=timezone.now().date()),
            Activity(user=users[1], type='Cycling', duration=45, calories=400, date=timezone.now().date()),
            Activity(user=users[3], type='Swimming', duration=60, calories=500, date=timezone.now().date()),
        ]
        for activity in activities:
            activity.save()

        # Create workouts
        workouts = [
            Workout(name='Hero HIIT', description='High intensity for heroes', suggested_for='Marvel'),
            Workout(name='Power Lifting', description='Strength for DC heroes', suggested_for='DC'),
        ]
        for workout in workouts:
            workout.save()

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=1200, rank=1)
        Leaderboard.objects.create(team=dc, points=1100, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
