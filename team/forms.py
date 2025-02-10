from django import forms

from account.models import Worker
from team.models import Team


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = (
            "name",
            "members",
        )
        widgets = {
            "members": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields["members"].queryset = Worker.objects.all()
            self.fields["members"].initial = [user]
