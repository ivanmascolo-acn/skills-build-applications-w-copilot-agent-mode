from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='test', email='test@test.com', password='pass')
        self.assertEqual(user.email, 'test@test.com')

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='TestTeam')
        self.assertEqual(team.name, 'TestTeam')

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        activity = Activity.objects.create(name='Run', user='test', team='TestTeam')
        self.assertEqual(activity.name, 'Run')

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='TestTeam', points=10)
        self.assertEqual(leaderboard.points, 10)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        self.assertEqual(workout.name, 'Pushups')
