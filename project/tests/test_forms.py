from django.test import TestCase
from django.contrib.auth import get_user_model

from account.models import Position
from project.forms import ProjectForm
from project.models import Project
from team.models import Team


class ProjectFormTest(TestCase):

    def test_team_queryset_filtered_by_user(self):
        position = Position.objects.create(
            name="test",
        )
        test_user1 = get_user_model().objects.create_user(
            username="testuser", password="password", position=position
        )
        test_team1 = Team.objects.create(name="Test Team", author=test_user1)
        test_user2 = get_user_model().objects.create_user(
            username="otheruser", password="password", position=position
        )
        test_team2 = Team.objects.create(name="Other Team", author=test_user2)

        form = ProjectForm(user=test_user1)
        self.assertIn(test_team1, form.fields["team"].queryset)
        self.assertNotIn(test_team2, form.fields["team"].queryset)
