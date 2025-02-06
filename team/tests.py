from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from account.models import Position
from team.models import Team


class TeamViewTest(TestCase):
    def setUp(self):
        position = Position.objects.create(name="test")
        self.user1 = get_user_model().objects.create_user(
            username="test1",
            password="test1",
            position=position,
        )
        self.user2 = get_user_model().objects.create_user(
            username="test2",
            password="test2",
            position=position,
        )
        self.user3 = get_user_model().objects.create_user(
            username="test3",
            password="test3",
            position=position,
        )

        self.user4 = get_user_model().objects.create_user(
            username="test4",
            password="test4",
            position=position,
        )

        self.team1 = Team.objects.create(
            name="test",
            author=self.user1,
        )
        self.team1.members.add(self.user1, self.user2)

        self.team2 = Team.objects.create(
            name="test2",
            author=self.user3,
        )
        self.team2.members.add(self.user2, self.user3)

    def test_team_view(self):
        self.client.force_login(self.user1)
        url = reverse("team:team-list")
        response = self.client.get(url)
        self.assertEqual(list(response.context["team_list"]), [self.team1])

    def test_auto_add_author(self):
        self.client.force_login(self.user1)
        url = reverse("team:team-create")
        data = {
            "name": "test",
        }
        response = self.client.post(url, data)
        self.assertEqual(Team.objects.count(), 3)

        team = Team.objects.last()
        self.assertEqual(team.author, self.user1)
