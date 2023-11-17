from django.urls import path
from . import views


urlpatterns = [
    path('company-list/', views.CompanyList.as_view(), name='company-list'),
    path('company-top/', views.CompanyTop.as_view(), name='company-top'),
    path('company-detail/', views.CompanyDetail.as_view(), name='company-detail'),
]
