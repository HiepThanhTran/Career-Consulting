from django.urls import path

from . import views


urlpatterns = [
    path('api/verification-email/', views.SendVerificationEmailView.as_view(), name='verification_email'),
]
