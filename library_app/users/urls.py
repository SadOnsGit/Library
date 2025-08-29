from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import CustomLoginView, UserCreateView, ProfileTemplateView

app_name = 'users'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('registration/', UserCreateView.as_view(), name='registration'),
    path('profile/', ProfileTemplateView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout')
]
