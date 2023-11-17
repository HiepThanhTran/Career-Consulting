from django.urls import path
from . import views


urlpatterns = [
    path('change-password/', views.ChangePassword.as_view(), name='change-password'),
    path('job-settings/', views.JobSettings.as_view(), name='job-settings'),
    path('profile-settings/', views.ProfileSettings.as_view(), name='profile-settings'),
]
