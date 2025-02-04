from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from account.models import Worker
from project.models import Project
from task.forms import TaskForm
from task.models import Task


class Index(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "task_pages/home_page.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        context["not_completed"] = self.get_queryset().filter(
            assignee=self.request.user, is_completed=False
        )
        context["completed"] = self.get_queryset().filter(
            assignee=self.request.user, is_completed=True
        )
        return context


class CreatedTaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "task_pages/created_task_list.html"

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)



@login_required
def create_task_view(request, project_id = None):
    project = get_object_or_404(Project, pk=project_id) if project_id else None

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.project = project
            task.save()
            return redirect("project:project-detail", pk=project.id) if project_id else redirect("task:task-list-created")
    else:
        form = TaskForm()
        if project:
            form.fields["assignee"].queryset = Project.objects.get(id=project.id).team.members.all()
        else:
            form.fields["assignee"].queryset = Worker.objects.all()

    return render(request, "task_pages/task_form.html", {"form": form, "project": project})


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"
    template_name = "task_pages/task_detail.html"


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_pages/task_form.html"
    success_url = reverse_lazy("task:task-list-created")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("task:task-list-created")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("task:task"))
