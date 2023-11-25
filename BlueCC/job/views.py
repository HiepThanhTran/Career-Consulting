from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


class SuitableJob(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.has_perm('company.view_company'):
            redirect_to = request.path
            login_url = reverse('login')
            message = 'Vui lòng đăng nhập vào tài khoản người dùng bình thường'
            return redirect(f'{login_url}?next={redirect_to}&message={message}')

        return render(request, template_name='job/suitable_job.html')

    def post(self, request):
        pass


class AppliedJob(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.has_perm('company.view_company'):
            redirect_to = request.path
            login_url = reverse('login')
            message = 'Vui lòng đăng nhập vào tài khoản người dùng bình thường'
            return redirect(f'{login_url}?next={redirect_to}&message={message}')

        return render(request, template_name='job/applied_job.html')

    def post(self, request):
        pass


class SavedJob(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.has_perm('company.view_company'):
            redirect_to = request.path
            login_url = reverse('login')
            message = 'Vui lòng đăng nhập vào tài khoản người dùng bình thường'
            return redirect(f'{login_url}?next={redirect_to}&message={message}')

        return render(request, template_name='job/saved_job.html')

    def post(self, request):
        pass


class SearchJob(View):
    def get(self, request):
        return render(request, template_name='job/search_job.html')

    def post(self, request):
        pass
