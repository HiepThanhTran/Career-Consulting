from django.urls import path
from . import views


urlpatterns = [
    path('suitable-job/', views.SuitableJob.as_view(), name='suitable-job'),
    path('applied-job/', views.AppliedJob.as_view(), name='applied-job'),
    path('saved-job/', views.SavedJob.as_view(), name='saved-job'),
    path('search-job/', views.SearchJob.as_view(), name='search-job'),
]