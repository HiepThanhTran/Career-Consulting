import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from job.models import JobDescription, JobApplication
from user.models import User


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

        jas = JobApplication.objects.filter(user=request.user.user)

        return render(request, template_name='job/applied_job.html', context={
            'jas': jas,
        })


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
        jobs = JobDescription.objects.all().order_by('-updated_date')

        return render(request, template_name='job/search_job.html', context={
            'jobs': jobs,
        })

    def post(self, request):
        pass


class DetailJob(View):
    def get(self, request, jobdescription_id=None):
        has_applied = True
        try:
            jd = JobDescription.objects.get(pk=jobdescription_id)
        except ObjectDoesNotExist:
            return redirect('page404')
        else:
            if request.user.is_authenticated and not request.user.has_perm('company.view_company') and not request.user.is_superuser:
                has_applied = JobApplication.objects.filter(user=request.user.user, job=jd).exists()

        return render(request, template_name='job/detail_job.html', context={
            'jd': jd,
            'has_applied': has_applied
        })


class ApplyJob(View):
    def post(self, request):
        data = json.load(request)
        user = User.objects.get(pk=data.get('userID'))
        job = JobDescription.objects.get(pk=data.get('jobID'))

        ja = JobApplication(user=user, job=job)
        ja.save()

        return JsonResponse({
            'redirect_to': '/job/applied-job/',
        })
