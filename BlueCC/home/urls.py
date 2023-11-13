from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('', include('users.urls')),
    path('', include('users.urls')),
    path('', include('users.urls')),
]
