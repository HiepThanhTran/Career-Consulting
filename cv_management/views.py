from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


class CVMajor(View):
    def get(self, request):
        return render(request, template_name='cv_management/cv_major.html')

    def post(self, request):
        pass


class CVManagement(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.has_perm('company.view_company'):
            redirect_to = request.path
            login_url = reverse('login')
            message = 'Vui lòng đăng nhập vào tài khoản người dùng bình thường'
            return redirect(f'{login_url}?next={redirect_to}&message={message}')

        return render(request, template_name='cv_management/cv_management.html')

    def post(self, request):
        pass


class UploadCV(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, template_name='cv_management/upload_cv.html')

    def post(self, request):
        pass


class CVTemplate(View):
    def get(self, request):
        return render(request, template_name='cv_management/cv_template.html')

    def post(self, request):
        pass
