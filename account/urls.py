from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import CustomLoginView, no_permission_view

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("no-permission/", no_permission_view, name="no-permission"),
]

app_name = "account"