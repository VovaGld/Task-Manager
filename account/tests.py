from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from account.models import Position

LOGIN_URL = reverse("account:login")


class AccountTestClass(TestCase):
    def setUp(self):
        position = Position.objects.create(name="test")
        self.user = get_user_model().objects.create_user(
            username="testname",
            password="testpassword",
            position=position,
        )

    def test_remember_me_enabled(self):
        response = self.client.post(
            LOGIN_URL,
            {"username": "testname", "password": "testpassword", "remember_me": True},
        )
        self.assertEqual(self.client.session.get_expiry_age(), settings.EXPIRY_TIME)
