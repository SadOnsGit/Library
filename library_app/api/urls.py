from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BookViewSet

v1_router = DefaultRouter()
v1_router.register('book', BookViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls))
]
