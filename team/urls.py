from django.urls import path

from team.views import (
    TeamListView,
    TeamCreateView,
    TeamUpdateView,
    TeamDeleteView,
    TeamDetailView,
)

urlpatterns = [
    path("", TeamListView.as_view(), name="team-list"),
    path("create/", TeamCreateView.as_view(), name="team-create"),
    path("detail/<int:pk>/", TeamDetailView.as_view(), name="team-detail"),
    path("update/<int:pk>", TeamUpdateView.as_view(), name="team-update"),
    path("delete/<int:pk>", TeamDeleteView.as_view(), name="team-delete"),
]

app_name = "team"
