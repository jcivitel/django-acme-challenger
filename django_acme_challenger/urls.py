from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("acme-challenge/", include("django_acme_backend.urls")),
]
