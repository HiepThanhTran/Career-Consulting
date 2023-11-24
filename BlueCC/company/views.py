import json

from allauth.account.models import EmailAddress
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import Permission

from company.forms import UploadRecruitmentForm, CompanySettingsForm
from company.models import Company
from home.models import Account
from home.utils import is_safe_url


class CompanyLogin(View):
    def get(self, request):
        message = request.GET.get('message', None)
        return render(request, template_name='company/company_login.html', context={
            'message': message
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
        return render(request, template_name='company/company_signup.html')

    def post(self, request):
        data = json.load(request)
        company_name = data.get('companyName')
        email = data.get('email')
        phone_number = data.get('phone')
        password = data.get('password')

        account = Account.objects.create_user(username=email, email=email, password=password)
        account.phone_number = phone_number
        permission = Permission.objects.get(codename='view_company')
        account.user_permissions.add(permission)
        account.save()
        EmailAddress.objects.add_email(request, account, account.email)
        company = Company(account=account, company_name=company_name)
        company.save()

        return JsonResponse({
            'message': 'Bạn đã đăng ký tài khoản thành công ở BlueCC. Bạn có thể đăng nhập ngay bây giờ!',
            'message_status': True,
        })


class CompanySettings(LoginRequiredMixin, View):
    login_url = 'company_login'

    def get(self, request):
        if not request.user.has_perm('company.view_company'):
            redirect_to = request.path
            login_url = reverse('company_login')
            message = 'Vui lòng đăng nhập vào tài khoản doanh nghiệp để sử dụng chức năng này'
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
            'picture': request.FILES.get('picture', None),
        }

        for field_name, field_value in data.items():
            if field_value:
                if field_name == 'phone_number':
                    request.user.phone_number = field_value
                    request.user.save()
                setattr(request.user.company, field_name, field_value)

        request.user.company.save()

        message = 'Cập nhật thông tin thành công!'

        return render(request, template_name='company/company_settings.html', context={
            'message': message,
            'form': form,
        })


class CompanyRecruitment(LoginRequiredMixin, View):
    login_url = 'company_login'

    def get(self, request):
        if not request.user.has_perm('company.view_company'):
            redirect_to = request.path
            login_url = reverse('company_login')
            message = 'Vui lòng đăng nhập vào tài khoản doanh nghiệp để sử dụng chức năng này'
            return redirect(f'{login_url}?next={redirect_to}&message={message}')

        form = UploadRecruitmentForm()

        return render(request, template_name='company/company_recruitment.html', context={
            'form': form
        })

    def post(self, request):
        pass


class CompanyList(View):
    def get(self, request):
        return render(request, template_name='company/company_list.html')

    def post(self, request):
        pass


class CompanyTop(View):
    def get(self, request):
        return render(request, template_name='company/company_top.html')

    def post(self, request):
        pass


class CompanyDetail(View):
    def get(self, request):
        return render(request, template_name='company/company_detail.html')

    def post(self, request):
        pass
