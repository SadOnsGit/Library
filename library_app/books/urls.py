from django.urls import path

from .views import BookView

app_name = 'book'

urlpatterns = [
    path('', BookView.as_view(), name='books'),
    path('search/', BookView.as_view(), name='search'),
]
