from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import CustomLoginView

app_name = 'users'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    # path('registration/', views.registration, name='registration'),
    # path('profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout')
]
