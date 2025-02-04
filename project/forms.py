from django import forms

from project.models import Project
from task.forms import TaskForm
from team.models import Team


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', "team"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['team'].queryset = Team.objects.filter(author=user)


# class TaskForProjectForm(TaskForm):

