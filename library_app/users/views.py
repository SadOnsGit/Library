from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

from .forms import UserLoginForm


class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True
