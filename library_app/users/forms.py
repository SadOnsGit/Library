from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser

class UserLoginForm(AuthenticationForm):

    class Meta:
        model = CustomUser
