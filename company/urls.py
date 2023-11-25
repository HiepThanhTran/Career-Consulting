from django.urls import path, re_path
from . import views


urlpatterns = [
    path('company/company-login/', views.CompanyLogin.as_view(), name='company_login'),
    path('company/company-signup/', views.CompanySignUp.as_view(), name='company_signup'),
    path('company/company-settings/<slug:slug>', views.CompanySettings.as_view(), name='company_settings'),
    path('company/company-recruitment/<slug:slug>', views.CompanyRecruitment.as_view(), name='company_recruitment'),
    path('company/company-recruitment-detail/<slug:slug>', views.CompanyRecruitmentDetail.as_view(),
         name='company_recruitment_detail'),
    path('company/company-recruitment-management/<slug:slug>', views.CompanyRecruitmentManagement.as_view(),
         name='company_recruitment_management'),
    path('company/company-recruitment-management-delete/', views.CompanyRecruitmentDetele.as_view(),
         name='company_recruitment_management_delete'),
    path('company/company-list/', views.CompanyList.as_view(), name='company_list'),
    path('company/company-top/', views.CompanyTop.as_view(), name='company_top'),
    path('company/company-detail/<slug:slug>', views.CompanyDetail.as_view(), name='company_detail'),
]
