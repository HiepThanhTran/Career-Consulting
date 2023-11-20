from django.urls import path
from . import views


urlpatterns = [
    path('job/suitable-job/', views.SuitableJob.as_view(), name='suitable_job'),
    path('job/applied-job/', views.AppliedJob.as_view(), name='applied_job'),
    path('job/saved-job/', views.SavedJob.as_view(), name='saved_job'),
    path('job/search-job/', views.SearchJob.as_view(), name='search_job'),
]