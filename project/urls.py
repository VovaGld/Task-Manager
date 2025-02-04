from django.urls import path

from project.views import ProjectListView, ProjectCreateView, ProjectDetailView, ProjectDeleteView, ProjectUpdateView

urlpatterns = [
    path("", ProjectListView.as_view(), name="project-list"),
    path("create/", ProjectCreateView.as_view(), name="project-create"),
    path("project-detail/<int:pk>", ProjectDetailView.as_view(), name="project-detail"),
    path("delete/<int:pk>", ProjectDeleteView.as_view(), name="project-delete"),
    path("update/<int:pk>", ProjectUpdateView.as_view(), name="project-update"),
]

app_name = "project"