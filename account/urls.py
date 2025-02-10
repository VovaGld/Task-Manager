from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import CustomLoginView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

app_name = "account"
