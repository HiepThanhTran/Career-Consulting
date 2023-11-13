from django.urls import path
from . import views


urlpatterns = [
    path('change-password/', views.change_password, name='change-password'),
    path('job-settings/', views.job_settings, name='job-settings'),
    path('profile-settings/', views.profile_settings, name='profile-settings'),
]
