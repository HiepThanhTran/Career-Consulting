from allauth.account.models import EmailAddress
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views import View


class SendVerificationEmailView(View):
    def post(self, request):
        try:
            email_address = EmailAddress.objects.get(user=request.user, verified=False)
            email_address.send_confirmation(request)

            return JsonResponse({'message': 'Email xác minh đã được gửi lại. Vui lòng kiểm tra hòm thư!'})
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Email không tồn tại hoặc không hợp lệ'})
        except Exception as e:
            return JsonResponse({'message': 'Có lỗi xảy ra khi gửi email xác nhận'})
