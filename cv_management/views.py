from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
import cloudinary.uploader

from cv_management.models import CurriculumVitae


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

        user = request.user.user
        cvs = CurriculumVitae.objects.filter(user=user).order_by('-created_date')

        return render(request, template_name='cv_management/cv_management.html', context={
            'cvs': cvs,
        })

    def post(self, request):
        pass


class UploadCV(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, template_name='cv_management/upload_cv.html')

    def post(self, request):
        user = request.user.user
        cv_image = request.FILES.get('file_upload_cv', None)

        image = cloudinary.uploader.upload(cv_image)
        path = image['secure_url']

        cv = CurriculumVitae(user=user, image=path)
        cv.save()

        return redirect('cv_management')


class CVTemplate(View):
    def get(self, request):
        return render(request, template_name='cv_management/cv_template.html')

    def post(self, request):
        pass
