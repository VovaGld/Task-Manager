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


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_pages/task_form.html"
    success_url = reverse_lazy("task:task")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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
