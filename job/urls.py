from django.urls import path
from . import views


urlpatterns = [
    path('job/suitable-job/', views.SuitableJob.as_view(), name='suitable_job'),
    path('job/applied-job/', views.AppliedJob.as_view(), name='applied_job'),
    path('job/apply-job/', views.ApplyJob.as_view(), name='apply_job'),
    path('job/saved-job/', views.SavedJob.as_view(), name='saved_job'),
    path('job/search-job/', views.SearchJob.as_view(), name='search_job'),
    path('job/detail-job/<int:jobdescription_id>', views.DetailJob.as_view(), name='detail_job'),
]