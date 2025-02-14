from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
)

from project.forms import ProjectForm
from project.mixins import TeamListMixin
from project.models import Project


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = "projects"
    template_name = "project/project_list.html"

    def get_queryset(self):
        return Project.objects.filter(team__members=self.request.user)


class ProjectCreateView(LoginRequiredMixin, TeamListMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "project/project_form.html"
    success_url = reverse_lazy("project:project-list")


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    context_object_name = "project"
    template_name = "project/project_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["tasks"] = self.get_object().tasks.all()

        return context


class ProjectUpdateView(LoginRequiredMixin, TeamListMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "project/project_form.html"
    success_url = reverse_lazy("project:project-list")


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy("project:project-list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)
