from django.urls import path
from . import views, admin

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('admin/', admin.admin_site.urls),
]
