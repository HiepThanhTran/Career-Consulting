from django.urls import path
from . import views


urlpatterns = [
    path('sign-in/', views.user_signin, name='sign-in'),
    path('sign-out', views.user_signout, name='sign-out'),
    path('sign-up/', views.user_register, name='sign-up'),
    path('forgot-password/', views.user_forgot_password, name='forgot-password'),
]
