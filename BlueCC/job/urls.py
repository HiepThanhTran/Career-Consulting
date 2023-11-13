from django.urls import path
from . import views


urlpatterns = [
    path('suitable-job/', views.suitable_job, name='suitable-job'),
    path('applied-job/', views.applied_job, name='applied-job'),
    path('saved-job/', views.saved_job, name='saved-job'),
    path('search-job/', views.search_job, name='search-job'),
]