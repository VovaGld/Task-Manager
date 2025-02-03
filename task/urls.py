from django.urls import path

from task.views import (
    Index,
    TaskCreateView,
    complete_task,
    CreatedTaskListView,
    TaskUpdateView,
    TaskDeleteView,
    TaskDetailView,
)

urlpatterns = [
    path("", Index.as_view(), name="task"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/created-list/", CreatedTaskListView.as_view(), name="task-list-created"),
    path("task/update/<int:pk>", TaskUpdateView.as_view(), name="task-update"),
    path("task/delete/<int:pk>", TaskDeleteView.as_view(), name="task-delete"),
    path("task/detail/<int:pk>", TaskDetailView.as_view(), name="task-detail"),
    path("task/<int:pk>/complete/", complete_task, name="task-complete"),
]

app_name = "task"
