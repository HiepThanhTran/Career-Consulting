from django.urls import path, re_path
from . import views


urlpatterns = [
    path('company/company-login/', views.CompanyLogin.as_view(), name='company_login'),
    path('company/company-signup/', views.CompanySignUp.as_view(), name='company_signup'),
    path('company/company-settings/', views.CompanySettings.as_view(), name='company_settings'),
    path('company/company-recruitment/', views.CompanyRecruitment.as_view(), name='company_recruitment'),
    path('company/company-recruitment-detail/<int:jobdescription_id>', views.CompanyRecruitmentDetail.as_view(),
         name='company_recruitment_detail'),
    path('company/company-recruitment-management/', views.CompanyRecruitmentManagement.as_view(),
         name='company_recruitment_management'),
    path('company/company-recruitment-management-delete/', views.CompanyRecruitmentDetele.as_view(),
         name='company_recruitment_management_delete'),
    path('company/company-list/', views.CompanyList.as_view(), name='company_list'),
    path('company/company-top/', views.CompanyTop.as_view(), name='company_top'),
    path('company/company-detail/<int:company_id>', views.CompanyDetail.as_view(), name='company_detail'),
]
