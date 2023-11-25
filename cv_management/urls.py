from django.urls import path, re_path
from . import views


urlpatterns = [
    path('cv/cv-major/', views.CVMajor.as_view(), name='cv_major'),
    path('cv/cv-template/', views.CVTemplate.as_view(), name='cv_template'),
    path('cv/cv-management/', views.CVManagement.as_view(), name='cv_management'),
    path('cv/cv-management/upload-cv/', views.UploadCV.as_view(), name='upload_cv'),
]
