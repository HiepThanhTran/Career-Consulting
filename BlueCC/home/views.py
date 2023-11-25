import json

from allauth.account.models import EmailAddress
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from company.models import Company
from home.models import Account
from job.models import JobDescription


class Home(View):
    def get(self, request):
        jobs = JobDescription.objects.all().order_by('-updated_date')[:6]
        latest_companies = Company.objects.all().order_by('-account__date_joined')[:6]

        return render(request, template_name='home/index.html', context={
            'jobs': jobs,
            'companies': latest_companies,
        })


class Page404(View):
    def get(self, request):
        return render(request, template_name='home/page404.html')


class SendVerificationEmailView(View):
    def post(self, request):
        data = json.load(request)
        email = data.get('email')
        try:
            account = Account.objects.filter(email=email).first()
            email_address = EmailAddress.objects.filter(user=account).first()
            if account and not email_address.verified:
                email_address.send_confirmation(request)
                return JsonResponse({'message': 'Email xác minh đã được vào hòm thư. Vui lòng kiểm tra hòm thư của bạn!'})
            else:
                return JsonResponse({'message': ''})
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Email không tồn tại hoặc không hợp lệ'})
        except Exception as e:
            return JsonResponse({'message': 'Có lỗi xảy ra khi gửi email xác nhận'})
