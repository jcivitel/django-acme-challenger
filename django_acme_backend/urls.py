from django.urls import path
from . import views

urlpatterns = [
    path('create-challenge/<int:domain_id>/', views.create_challenge, name='create_challenge'),
    path('list-domains/', views.list_domains, name='list_domains'),
]