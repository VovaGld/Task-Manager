from django.urls import path

from task.views import (
    Index,
    complete_task,
    CreatedTaskListView,
    TaskUpdateView,
    TaskDeleteView,
    TaskDetailView,
    create_task_view,
)

urlpatterns = [
    path("", Index.as_view(), name="task"),
    path("task/create/", create_task_view, name="task-create"),
    path("task/create/<int:project_id>/", create_task_view, name="task-project-create"),
    path("task/created-list/", CreatedTaskListView.as_view(), name="task-list-created"),
    path("task/update/<int:pk>", TaskUpdateView.as_view(), name="task-update"),
    path("task/delete/<int:pk>", TaskDeleteView.as_view(), name="task-delete"),
    path("task/detail/<int:pk>", TaskDetailView.as_view(), name="task-detail"),
    path("task/<int:pk>/complete/", complete_task, name="task-complete"),
]

app_name = "task"
