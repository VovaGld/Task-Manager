from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.management.base import BaseCommand
from django.conf import settings
from account.models import Position



class Command(BaseCommand):
    help = "Set random prices for existing movies"

    def handle(self, *args, **kwargs):
        User: type[AbstractUser] = get_user_model()
        new_user_username = settings.ADMIN_USERNAME
        new_user_email = settings.ADMIN_EMAIL
        new_user_password = settings.ADMIN_PASSWORD
        position = settings.POSITION

        user = User.objects.filter(username=new_user_username).first()

        if user:
            self.stdout.write(
                self.style.SUCCESS(f"User {new_user_username} is already exists.")
            )
        else:
            position_instance = Position.objects.get_or_create(
                name=position,
            )
            user = User(
                username=new_user_username,
                email=new_user_email,
                is_staff=True,
                is_superuser=True,
                position=position_instance,
            )
            user.set_password(new_user_password)
            user.save()

            self.stdout.write(
                    self.style.SUCCESS(f"User {new_user_username} created.")
                )
