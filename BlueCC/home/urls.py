from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('admin/', admin.site.urls, name='admin_site'),
    path('api/verification-email/', views.SendVerificationEmailView.as_view(), name='verification_email'),
]
