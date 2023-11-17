from django.urls import path
from . import views


urlpatterns = [
    path('sign-in/', views.UserSignin.as_view(), name='sign-in'),
    path('sign-out/', views.UserSignout.as_view(), name='sign-out'),
    path('sign-up/', views.UserRegister.as_view(), name='sign-up'),
    path('forgot-password/', views.UserForgotPassword.as_view(), name='forgot-password'),
]
