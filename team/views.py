from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from team.forms import TeamForm
from team.models import Team


class TeamListView(LoginRequiredMixin, ListView):
    model = Team
    template_name = "team_pages/team_list.html"

    def get_queryset(self):
        return Team.objects.filter(members=self.request.user)


class TeamCreateView(LoginRequiredMixin, CreateView):
    model = Team
    template_name = "team_pages/team_form.html"
    form_class = TeamForm
    success_url = reverse_lazy("team:team-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TeamDetailView(LoginRequiredMixin, DetailView):
    model = Team
    template_name = "team_pages/team_detail.html"


class TeamUpdateView(LoginRequiredMixin, UpdateView):
    model = Team
    template_name = "team_pages/team_form.html"
    form_class = TeamForm
    success_url = reverse_lazy("team:team-list")


class TeamDeleteView(LoginRequiredMixin, DeleteView):
    model = Team
    success_url = reverse_lazy("team:team-list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)
