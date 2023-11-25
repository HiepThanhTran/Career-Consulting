from django.urls import path, re_path
from . import views


urlpatterns = [
    path('account/login/', views.UserLogin.as_view(), name='login'),
    path('account/logout/', views.UserSignOut.as_view(), name='logout'),
    path('account/signup/', views.UserSignUp.as_view(), name='signup'),
    path('account/reset-password/', views.UserResetPassword.as_view(), name='reset_password'),
    re_path(r'^password\\-reset/(?P<uidb64>[^/]+)/(?P<token>[^/]+)/\\Z$', views.UserSetPassword.as_view(), name='set_password'),
]
