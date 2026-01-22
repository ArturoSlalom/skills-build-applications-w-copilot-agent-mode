from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=team)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.team.name, 'Test Team')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Team Alpha')
        self.assertEqual(team.name, 'Team Alpha')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='Team Beta')
        user = User.objects.create_user(username='user2', email='user2@example.com', password='pass', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=30, distance=5.0)
        self.assertEqual(activity.type, 'run')
        self.assertEqual(activity.duration, 30)
        self.assertEqual(activity.distance, 5.0)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        team = Team.objects.create(name='Team Gamma')
        user = User.objects.create_user(username='user3', email='user3@example.com', password='pass', team=team)
        workout = Workout.objects.create(user=user, name='Cardio', description='Cardio session', duration=45)
        self.assertEqual(workout.name, 'Cardio')
        self.assertEqual(workout.duration, 45)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Team Delta')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.team.name, 'Team Delta')
        self.assertEqual(leaderboard.points, 100)
