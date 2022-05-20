from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', include('authentication.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls)
]
