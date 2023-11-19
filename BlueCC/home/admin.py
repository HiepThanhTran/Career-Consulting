from django.utils.safestring import mark_safe

from home.forms import CompanyForm, JDForm
from job.models import *
from company.models import *
from django.contrib import admin
from cv_management.models import *


class CompanyAdminView(admin.ModelAdmin):
    form = CompanyForm

    list_display = ['id', 'name', 'industry', 'followers', 'active', 'created_date']
    list_filter = ['name', 'industry', 'created_date']
    search_fields = ['name', 'industry']
    readonly_fields = ['avatar_image']

    def avatar_image(self, obj):
        if obj:
            return mark_safe(
                "<img src='/static/images/{url}' width='120px' />".format(url=obj.avatar.name)
            )


class CVAdminView(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'active', 'created_date', 'updated_date']
    list_filter = ['name', 'created_date', 'updated_date']
    search_fields = ['name', 'user__name']
    readonly_fields = ['cv_image']

    def cv_image(self, obj):
        if obj:
            return mark_safe(
                "<img src='/static/images/{url}' width='120px' />".format(url=obj.avatar.name)
            )


class JobApplicationAdminView(admin.ModelAdmin):
    list_display = ['id', 'user', 'job', 'active', 'application_date']
    search_fields = ['user__name', 'job__name']


class JDAdminView(admin.ModelAdmin):
    form = JDForm

    list_display = ['id', 'name', 'deadline', 'company', 'active', 'created_date', 'updated_date']
    list_filter = ['name', 'deadline', 'created_date', 'updated_date']
    search_fields = ['name', 'company__name']


class UserAdminView(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login']
    list_filter = ['date_joined', 'last_login']
    search_fields = ['full_name', 'email']
    readonly_fields = ['avatar_image']

    def avatar_image(self, obj):
        if obj:
            return mark_safe(
                "<img src='/static/images/{url}' width='120px' />".format(url=obj.avatar.name)
            )


class BlueCCAppAdminSite(admin.AdminSite):
    site_title = 'BlueCC'
    site_header = 'Hệ thống hỗ trợ tìm việc làm | BlueCC'
    index_title = 'Trang quản trị'


# admin_site = BlueCCAppAdminSite(name='myadmin')


admin.site.register(Company, CompanyAdminView)
admin.site.register(CurriculumVitae, CVAdminView)
admin.site.register(JobApplication, JobApplicationAdminView)
admin.site.register(JobDescription, JDAdminView)
admin.site.register(User, UserAdminView)
