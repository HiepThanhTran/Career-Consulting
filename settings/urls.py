from django.urls import path

from . import views

urlpatterns = [
    path('settings/password-change/', views.ChangePassword.as_view(), name='password_change'),
    path('settings/job-settings/', views.JobSettings.as_view(), name='job_settings'),
    path('settings/profile-settings/', views.ProfileSettings.as_view(), name='profile_settings'),
]
