from django.shortcuts import render
from django.views import View


class ChangePassword(View):
    def get(self, request):
        return render(request, template_name='settings/change_password.html')

    def post(self, request):
        pass


class JobSettings(View):
    def get(self, request):
        return render(request, template_name='settings/job_settings.html')

    def post(self, request):
        pass


class ProfileSettings(View):
    def get(self, request):
        return render(request, template_name='settings/profile_settings.html')

    def post(self, request):
        pass
