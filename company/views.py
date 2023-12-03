import json
from datetime import datetime

import cloudinary.uploader
from allauth.account.models import EmailAddress
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import Permission

from company.forms import UploadRecruitmentForm, CompanySettingsForm
from company.models import Company
from home.models import Account
from home.utils import is_safe_url
from job.models import JobDescription


class CompanyLogin(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.has_perm('company.view_company'):
            return redirect('home')

        message = request.GET.get('message', None)

        return render(request, template_name='company/company_login.html', context={
            'message': message,
        })

    def post(self, request):
        data = json.load(request)
        email = data.get('email')
        password = data.get('password')
        redirect_to = data.get('params')
        account = authenticate(request, username=email, password=password)

        if account:
            logout(request)
            login(request, account)

            if is_safe_url(url=redirect_to, allowed_hosts=request.get_host()):
                return JsonResponse({'redirect_to': redirect_to})

        message = 'Email hoặc mật khẩu không chính xác!'

        return JsonResponse({
            'message': message,
            'message_status': False,
        })


class CompanySignUp(View):
    def get(self, request):
        return render(request, template_name='company/company_signup.html', context={

        })

    def post(self, request):
        data = json.load(request)
        company_name = data.get('companyName')
        email = data.get('email')
        phone_number = data.get('phone')
        password = data.get('password')

        message_status = False

        if Account.objects.filter(email=email).exists():
            message = 'Email doanh nghiệp đã tồn tại'
        elif Company.objects.filter(company_name=company_name).exists():
            message = 'Tên doanh nghiệp đã tồn tại'
        else:
            permission = Permission.objects.get(codename='view_company')
            account = Account.objects.create_user(username=email, email=email, password=password)
            account.phone_number = phone_number
            account.user_permissions.add(permission)
            account.save()
            EmailAddress.objects.add_email(request, account, account.email)
            company = Company(account=account, company_name=company_name)
            company.save()
            message = 'Bạn đã đăng ký tài khoản thành công ở BlueCC. Bạn có thể đăng nhập ngay bây giờ!'
            message_status = True

        return JsonResponse({
            'message': message,
            'message_status': message_status,
        })


class CompanySettings(LoginRequiredMixin, View):
    login_url = 'company_login'

    def get(self, request):
        if not request.user.has_perm('company.view_company') and not request.user.is_superuser:
            redirect_to = request.path
            login_url = reverse('company_login')
            message = 'Vui lòng đăng nhập vào tài khoản doanh nghiệp'
            return redirect(f'{login_url}?next={redirect_to}&message={message}')

        form = CompanySettingsForm()

        return render(request, template_name='company/company_settings.html', context={
            'form': form
        })

    def post(self, request):
        form = CompanySettingsForm()

        data = {
            'company_name': request.POST.get('company_name', None),
            'description': request.POST.get('description', None),
            'address': request.POST.get('address', None),
            'phone_number': request.POST.get('phone_number', None),
            'number_of_employees': request.POST.get('number_of_employees', None),
            'social_link': request.POST.get('social_link', None),
            'industry': request.POST.get('industry', None),
            'avatar': request.FILES.get('picture', None),
        }

        for field_name, field_value in data.items():
            if field_value:
                if field_name == 'phone_number':
                    setattr(request.user, field_name, field_value)
                    request.user.save()
                elif field_name == 'avatar':
                    path = cloudinary.uploader.upload(field_value)
                    request.user.avatar = path['secure_url']
                    request.user.save()
                else:
                    setattr(request.user.company, field_name, field_value)

        request.user.company.save()

        message = 'Cập nhật thông tin thành công!'

        return render(request, template_name='company/company_settings.html', context={
            'message': message,
            'form': form,
        })


class CompanyRecruitmentManagement(LoginRequiredMixin, View):
    login_url = 'company_login'

    def get(self, request):
        if not request.user.has_perm('company.view_company') and not request.user.is_superuser:
            redirect_to = request.path
            login_url = reverse('company_login')
            message = 'Vui lòng đăng nhập vào tài khoản doanh nghiệp'
            return redirect(f'{login_url}?next={redirect_to}&message={message}')

        company = request.user.company
        jds = JobDescription.objects.all().filter(company=company)

        return render(request, template_name='company/company_management.html', context={
            'jds': jds,
        })

    def post(self, request):
        pass


class CompanyRecruitment(LoginRequiredMixin, View):
    login_url = 'company_login'

    def get(self, request):
        if not request.user.has_perm('company.view_company') and not request.user.is_superuser:
            redirect_to = request.path
            login_url = reverse('company_login')
            message = 'Vui lòng đăng nhập vào tài khoản doanh nghiệp'
            return redirect(f'{login_url}?next={redirect_to}&message={message}')

        form = UploadRecruitmentForm()

        return render(request, template_name='company/company_recruitment.html', context={
            'form': form
        })

    def post(self, request):
        company = request.user.company
        name = request.POST.get('name', None)
        salary_start = request.POST.get('salary_start', None)
        salary_end = request.POST.get('salary_end', None)
        location = request.POST.get('location', None)
        experience_year = request.POST.get('experience_year', None)
        description = request.POST.get('description', None)
        requirements = request.POST.get('requirements', None)
        benefits = request.POST.get('benefits', None)
        deadline = request.POST.get('deadline', None)
        position = request.POST.get('position', None)
        number_of_recruits = request.POST.get('number_of_recruits', None)
        work_form = request.POST.get('work_form', None)
        gender = request.POST.get('gender', None)

        jd = JobDescription(company=company,
                            name=name,
                            salary_start=salary_start,
                            salary_end=salary_end,
                            location=location,
                            experience_year=experience_year,
                            description=description,
                            requirements=requirements,
                            benefits=benefits,
                            deadline=deadline,
                            position=position,
                            number_of_recruits=number_of_recruits,
                            work_form=work_form,
                            gender=gender)
        jd.save()

        return redirect('company_recruitment_management')


class CompanyRecruitmentDetail(LoginRequiredMixin, View):
    login_url = 'company_login'

    def get(self, request, jobdescription_id=None):
        jd = JobDescription.objects.get(pk=jobdescription_id)

        return render(request, template_name='company/company_recruitment_detail.html', context={
            'jd': jd,
        })

    def post(self, request, jobdescription_id=None):
        jobdescription_id = request.POST.get('jobdescription_id')
        jd = JobDescription.objects.get(pk=jobdescription_id)

        data = {
            'name': request.POST.get('name', None),
            'salary_start': request.POST.get('salary_start', None),
            'salary_end': request.POST.get('salary_end', None),
            'location': request.POST.get('location', None),
            'experience_year': request.POST.get('experience_year', None),
            'description': request.POST.get('description', None),
            'requirements': request.POST.get('requirements', None),
            'benefits': request.POST.get('benefits', None),
            'deadline': request.POST.get('deadline', None),
            'position': request.POST.get('position', None),
            'number_of_recruits': request.POST.get('number_of_recruits', None),
            'work_form': request.POST.get('work_form', None),
            'gender': request.POST.get('gender', None),
        }

        for field_name, field_value in data.items():
            if field_value:
                setattr(jd, field_name, field_value)

        jd.save()

        return redirect('company_recruitment_management')


class CompanyRecruitmentDetele(LoginRequiredMixin, View):
    login_url = 'company_login'

    def post(self, request):
        data = json.load(request)
        jobdescription_id = data.get('jobdescription_id', None)

        message = 'Xoá không thành công'
        message_status = False

        if jobdescription_id:
            jd = JobDescription.objects.get(pk=jobdescription_id)
            jd.delete()

            message = 'Xoá thành công'
            message_status = True

        return JsonResponse({
            'message': message,
            'message_status': message_status
        })


class CompanyList(View):
    def get(self, request):
        latest_companies = Company.objects.all().order_by('-account__date_joined')[:6]

        return render(request, template_name='company/company_list.html', context={
            'companies': latest_companies,
        })


class CompanyTop(View):
    def get(self, request):
        companies = Company.objects.all().order_by('-followers')[:6]

        return render(request, template_name='company/company_top.html', context={
            'companies': companies,
        })


class CompanyDetail(View):
    def get(self, request, company_id=None):
        try:
            company = Account.objects.get(pk=company_id)
            jds = JobDescription.objects.filter(company=company.company)
        except ObjectDoesNotExist:
            return redirect('page404')

        return render(request, template_name='company/company_detail.html', context={
            'company': company,
            'jds': jds,
        })

    def post(self, request):
        pass
