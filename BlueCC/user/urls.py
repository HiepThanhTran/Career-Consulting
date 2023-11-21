from django.urls import path, re_path
from . import views


urlpatterns = [
    path('account/login/', views.UserSignin.as_view(), name='login'),
    path('account/logout/', views.UserSignout.as_view(), name='logout'),
    path('account/signup/', views.UserRegister.as_view(), name='signup'),
    path('account/password-reset-request/', views.UserPasswordReset.as_view(), name='password_reset'),
    re_path(r'^password\\-reset/(?P<uidb64>[^/]+)/(?P<token>[^/]+)/\\Z$', views.PasswordSet.as_view(), name='password_set'),
]
