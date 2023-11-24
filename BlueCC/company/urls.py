from django.urls import path, re_path
from . import views


urlpatterns = [
    path('company/company-login/', views.CompanyLogin.as_view(), name='company_login'),
    path('company/company-signup/', views.CompanySignUp.as_view(), name='company_signup'),
    path('company/company-settings/', views.CompanySettings.as_view(), name='company_settings'),
    path('company/company-recruitment/', views.CompanyRecruitment.as_view(), name='company_recruitment'),
    path('company/company-list/', views.CompanyList.as_view(), name='company_list'),
    path('company/company-top/', views.CompanyTop.as_view(), name='company_top'),
    path('company/company-detail/', views.CompanyDetail.as_view(), name='company_detail'),
]
