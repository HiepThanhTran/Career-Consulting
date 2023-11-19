from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserSignin.as_view(), name='login'),
    path('logout/', views.UserSignout.as_view(), name='logout'),
    path('signup/', views.UserRegister.as_view(), name='signup'),
    path('password-reset/', views.UserPasswordReset.as_view(), name='password_reset'),
    path('activate/<uidb64>/<token>', views.Activate.as_view(), name='activate'),
]
