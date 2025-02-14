from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from account.models import Position
from project.models import Project
from task.models import Task, TaskType
from team.models import Team


class ViewTests(TestCase):
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

        self.project1 = Project.objects.create(
            name="test",
            description="test",
            team=self.team1,
            author=self.user1,
        )

        self.project2 = Project.objects.create(
            name="test2",
            description="test2",
            team=self.team2,
            author=self.user3,
        )

    def test_project_list(self):
        self.client.force_login(self.user1)
        url = reverse("project:project-list")
        response = self.client.get(url)
        self.assertEqual(list(response.context["projects"]), [self.project1])

        self.client.force_login(self.user2)
        response = self.client.get(url)
        self.assertEqual(
            list(response.context["projects"]), [self.project1, self.project2]
        )

        self.client.force_login(self.user4)
        response = self.client.get(url)
        self.assertEqual(list(response.context["projects"]), [])

    def test_auto_add_project_author(self):
        self.client.force_login(self.user1)
        url = reverse("project:project-create")
        response = self.client.post(
            url,
            {
                "name": "test",
                "description": "test",
                "team": self.team1.id,
            },
        )
        self.assertEqual(Project.objects.count(), 3)
        project = Project.objects.last()
        self.assertEqual(project.author, self.user1)

    def test_if_user_do_not_have_team(self):
        self.client.force_login(self.user4)
        url = reverse("project:project-create")
        response = self.client.get(url)
        self.assertRedirects(response, reverse("team:team-create"))

    def test_task_list_in_project_detail_view(self):
        task_type = TaskType.objects.create(
            name="test",
        )
        deadline = timezone.now() + timezone.timedelta(days=1)
        task1 = Task.objects.create(
            name="test1",
            description="test",
            task_type=task_type,
            deadline=deadline,
            project=self.project1,
            author=self.user1,
            priority=1,
        )
        task1.assignee.add(self.user2)
        task2 = Task.objects.create(
            name="test2",
            description="test",
            task_type=task_type,
            deadline=deadline,
            author=self.user1,
            priority=1,
        )
        task2.assignee.add(self.user3)
        task3 = Task.objects.create(
            name="test3",
            description="test",
            task_type=task_type,
            deadline=deadline,
            project=self.project2,
            author=self.user1,
            priority=1,
        )
        task3.assignee.add(self.user2)
        self.client.force_login(self.user1)
        url = reverse("project:project-detail", args=[self.project1.id])
        response = self.client.get(url)
        self.assertEqual(list(response.context["tasks"]), [task1])
