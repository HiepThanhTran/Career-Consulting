from django.urls import path
from . import views


urlpatterns = [
    path('cv-major/', views.cv_major, name='cv-major'),
    path('cv-management/', views.cv_management, name='cv-management'),
    path('cv-template/', views.cv_template, name='cv-template'),
]
