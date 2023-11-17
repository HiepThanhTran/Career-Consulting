from django.urls import path
from . import views


urlpatterns = [
    path('cv-major/', views.CVMajor.as_view(), name='cv-major'),
    path('cv-management/', views.CVManagement.as_view(), name='cv-management'),
    path('cv-template/', views.CVTemplate.as_view(), name='cv-template'),
]
