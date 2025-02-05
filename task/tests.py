from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from account.models import Position
from project.models import Project
from task.models import TaskType, Task
from team.models import Team

TASK_LIST_URL = reverse("task:task")
CREATED_TASK_LIST_URL = reverse("task:task-list-created")
TASK_CREATE_URL = reverse("task:task-create")

class TaskTests(TestCase):
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
        self.task_type = TaskType.objects.create(
            name="test",
        )
        self.task1 = Task.objects.create(
            name="test1",
            description="test",
            task_type=self.task_type,
            deadline=timezone.now() + timezone.timedelta(days=3),
            author=self.user1,
            priority=2,
        )
        self.task1.assignee.add(self.user2)
        self.task2 = Task.objects.create(
            name="test2",
            description="test",
            task_type=self.task_type,
            deadline=timezone.now() + timezone.timedelta(days=2),
            author=self.user1,
            priority=1,
            is_completed=True,
        )
        self.task2.assignee.add(self.user2)
        self.task3 = Task.objects.create(
            name="test3",
            description="test",
            task_type=self.task_type,
            deadline=timezone.now() + timezone.timedelta(days=1),
            author=self.user1,
            priority=3,
        )
        self.task3.assignee.add(self.user2)

    def test_task_list_view(self):
        self.client.force_login(self.user2)
        response = self.client.get(TASK_LIST_URL)
        self.assertEqual(list(response.context["tasks"]), [self.task1, self.task2, self.task3])

        self.client.force_login(self.user1)
        response = self.client.get(TASK_LIST_URL)
        self.assertEqual(list(response.context["tasks"]), [])

    def test_filter_completed_tasks(self):
        self.client.force_login(self.user2)
        response = self.client.get(TASK_LIST_URL + "?filter=completed")
        self.assertEqual(list(response.context["tasks"]), [self.task2])

    def test_filter_uncompleted_tasks(self):
        self.client.force_login(self.user2)
        response = self.client.get(TASK_LIST_URL + "?filter=uncompleted")
        self.assertEqual(list(response.context["tasks"]), [self.task1, self.task3])

    def test_order_tasks_by_priority(self):
        self.client.force_login(self.user2)
        response = self.client.get(TASK_LIST_URL + "?order=priority")
        self.assertEqual(list(response.context["tasks"]), [self.task2, self.task1, self.task3])

    def test_order_tasks_by_deadline(self):
        self.client.force_login(self.user2)
        response = self.client.get(TASK_LIST_URL + "?order=date")
        self.assertEqual(list(response.context["tasks"]), [self.task3, self.task2, self.task1])

    def test_created_task_view(self):
        self.client.force_login(self.user1)
        response = self.client.get(CREATED_TASK_LIST_URL)
        self.assertEqual(list(response.context["tasks"]), [self.task1, self.task2, self.task3])

    def test_created_task_search(self):
        self.client.force_login(self.user1)
        response = self.client.get(CREATED_TASK_LIST_URL + "?search=1")
        self.assertEqual(list(response.context["tasks"]), [self.task1])

    def test_auto_add_author(self):
        self.client.force_login(self.user1)
        data = {
            "name": "test",
            "description": "test",
            "priority": 2,
            "deadline": timezone.now() + timezone.timedelta(days=3),
            "assignee": self.user2,
        }
        response = self.client.post(TASK_CREATE_URL, data)
        task = Task.objects.last()
        self.assertEqual(task.author, self.user1)

