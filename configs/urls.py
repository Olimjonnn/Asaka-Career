
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('apps.main.urls')),
    path('', include('apps.career.urls')),
    path('', include('apps.blog.urls')),
    path('', include('apps.vacancy.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
