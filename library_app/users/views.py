from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import UserLoginForm, RegistrationForm


class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('user:profile')

    def get_success_url(self):
        return self.success_url


class UserCreateView(CreateView):
    form_class = RegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('books:index')


class ProfileTemplateView(TemplateView):
    template_name = 'users/profile.html'
