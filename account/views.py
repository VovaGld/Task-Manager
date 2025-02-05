from django.conf import settings
from django.contrib.auth.views import LoginView
from django.shortcuts import render

from account.forms import CustomAuthForm


class CustomLoginView(LoginView):
    form_class = CustomAuthForm

    def form_valid(self, form):
        response = super().form_valid(form)

        remember_me = form.cleaned_data.get("remember_me")
        if remember_me:
            self.request.session.set_expiry(settings.EXPIRY_TIME)

        else:
            self.request.session.set_expiry(0)

        return response

def no_permission_view(request):
    return render(request, "no_permission_massage.html")