from django.urls import path, re_path
from . import views

app_label = 'user'

urlpatterns = [
    path('login/', views.UserSignin.as_view(), name='login'),
    path('logout/', views.UserSignout.as_view(), name='logout'),
    path('signup/', views.UserRegister.as_view(), name='signup'),
    path('password-reset-request/', views.UserPasswordReset.as_view(), name='password_reset'),
    re_path(r'^activate/(?P<uidb64>[^/]+)/(?P<token>[^/]+)/\\Z$', views.Activate.as_view(), name='activate'),
    re_path(r'^password\\-reset/(?P<uidb64>[^/]+)/(?P<token>[^/]+)/\\Z$', views.PasswordSet.as_view(), name='password_set')
]
