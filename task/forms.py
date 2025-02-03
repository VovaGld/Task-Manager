from django import forms

from task.models import Task


class TaskForm(forms.ModelForm):
    priority = forms.ChoiceField(choices=Task.PRIORITY_CHOICES, widget=forms.Select())

    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "task_type",
            "deadline",
            "priority",
            "assignee",
        ]
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "datetime-local"}),
            "assignee": forms.CheckboxSelectMultiple(),
            "task_type": forms.RadioSelect(),
        }
