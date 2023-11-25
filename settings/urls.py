from django.urls import path

from . import views

urlpatterns = [
    path('settings/password-change/<slug:slug>', views.ChangePassword.as_view(), name='password_change'),
    path('settings/job-settings/<slug:slug>', views.JobSettings.as_view(), name='job_settings'),
    path('settings/profile-settings/<slug:slug>', views.ProfileSettings.as_view(), name='profile_settings'),
]
