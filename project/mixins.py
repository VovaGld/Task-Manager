from django.shortcuts import redirect
from django.views.generic import UpdateView

from team.models import Team


class TeamListMixin(UpdateView):
    def dispatch(self, request, *args, **kwargs):
        if not Team.objects.filter(author=request.user).exists():
            return redirect("team:team-create")
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
