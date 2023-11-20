from django.urls import path
from . import views


urlpatterns = [
    path('company/company-list/', views.CompanyList.as_view(), name='company_list'),
    path('company/company-top/', views.CompanyTop.as_view(), name='company_top'),
    path('company/company-detail/', views.CompanyDetail.as_view(), name='company_detail'),
]
