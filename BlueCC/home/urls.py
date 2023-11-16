from django.urls import path
from . import views, admin

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.admin_site.urls),
]
