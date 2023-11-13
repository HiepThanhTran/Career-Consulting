from django.urls import path
from . import views


urlpatterns = [
    path('company-list/', views.company_list, name='company-list'),
    path('company-top/', views.company_top, name='company-top'),
    path('company-detail/', views.company_detail, name='company-detail'),
]
