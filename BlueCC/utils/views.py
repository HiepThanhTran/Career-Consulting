import json

from allauth.account.models import EmailAddress
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views import View

from home.models import Account


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
