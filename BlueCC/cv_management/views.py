from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class CVMajor(View):
    def get(self, request):
        return render(request, template_name='cv_management/cv_major.html')

    def post(self, request):
        pass


class CVManagement(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, template_name='cv_management/cv_management.html')

    def post(self, request):
        pass


class CVTemplate(View):
    def get(self, request):
        return render(request, template_name='cv_management/cv_template.html')

    def post(self, request):
        pass
