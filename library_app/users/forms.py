from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import CustomUser


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = CustomUser


class RegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username',)
