from django.urls import path
from . import views


urlpatterns = [
    path('sign-in/', views.user_login, name='sign-in'),
    path('sign-up/', views.user_register, name='sign-up'),
    path('forgot-password/', views.user_forgot_password, name='forgot-password'),
]
