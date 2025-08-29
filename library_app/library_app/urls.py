from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('books/', include('books.urls', namespace='books')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('users.urls', namespace='user'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
