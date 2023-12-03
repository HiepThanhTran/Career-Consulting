import json

from allauth.account.models import EmailAddress
from django.http import JsonResponse
from django.urls import reverse
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from home.models import Account
from user.models import User
from django.views import View

from user.tokens import account_activation_token
from home.utils import is_safe_url, send_email_reset_password
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model


class UserLogin(View):
    def get(self, request):
        if request.user.is_authenticated and not request.user.has_perm('company.view_company'):
            return redirect('home')

        message = request.GET.get('message', None)

        return render(request, template_name='user/login.html', context={
            'message': message,
        })

    def post(self, request):
        data = json.load(request)
        email = data.get('email')
        password = data.get('password')
        redirect_to = data.get('params')
        account = authenticate(request, username=email, password=password)

        if account:
            login(request, account)

            if is_safe_url(url=redirect_to, allowed_hosts=request.get_host()):
                return JsonResponse({'redirect_to': redirect_to})

        message = 'Email hoặc mật khẩu không chính xác!'

        return JsonResponse({
            'message': message,
            'message_status': False,
        })


class UserSignOut(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class UserSignUp(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        return render(request, template_name='user/signup.html', context={

        })

    def post(self, request):
        data = json.load(request)
        full_name = data.get('fullName')
        email = data.get('email')
        password = data.get('password')

        if Account.objects.filter(email=email).exists():
            message = 'Tài khoản đã tồn tại. Vui lòng đăng nhập hoặc chọn email khác!'
            message_status = False
        else:
            account = Account.objects.create_user(username=email, email=email, password=password)
            user = User(account=account, full_name=full_name)
            user.save()
            EmailAddress.objects.add_email(request, account, account.email)
            message = 'Bạn đã đăng ký thành công tài khoản ở BlueCC. Bạn có thể đăng nhập ngay bây giờ!'
            message_status = True

        return JsonResponse({
            'message': message,
            'message_status': message_status,
        })


class UserResetPassword(View):
    def get(self, request):
        return render(request, template_name='user/reset_password.html')

    def post(self, request):
        data = json.load(request)
        email = data.get('email')

        account = Account.objects.filter(email=email).first()

        message = 'Tài khoản không tồn tại!' if not account else None
        message_status = False

        if account:
            mail_result = send_email_reset_password(request,
                                                    account=account,
                                                    to_email=email,
                                                    mail_subject='Password reset',
                                                    template='account/email/template_reset_password.html',
                                                    message_success='Đã gửi yêu cầu thay đổi mật khẩu đến email của bạn!')

            message = mail_result['message']
            message_status = mail_result['message_status']

        return JsonResponse({
            'message': message,
            'message_status': message_status,
        })


class UserSetPassword(View):
    def get(self, request, uidb64=None, token=None):
        user = get_user_model()
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = user.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, user.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            return render(request, template_name='user/set_password.html', context={
                'uid': uidb64,
                'token': token,
            })
        else:
            message_status = False
            message = 'Đường dẫn không hợp lệ!'

        return render(request, template_name='user/login.html', context={
            'message': message,
            'message_status': message_status,
        })

    def post(self, request, uidb64=None, token=None):
        user = get_user_model()
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = user.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, user.DoesNotExist):
            user = None

        message = 'Đường dẫn không hợp lệ!'
        message_status = False

        if user is not None and account_activation_token.check_token(user, token):
            new_password = request.POST['new_password'].strip()
            confirm_new_password = request.POST['confirm_new_password'].strip()
            url = request.build_absolute_uri()

            if new_password == confirm_new_password:
                user.set_password(new_password)
                user.save()
                message = 'Thay đổi mật khẩu thành công!'
                message_status = True
            else:
                message = 'Mật khẩu không khớp!'
                return redirect(reverse(url, kwargs={
                    'message': message,
                    'message_status': message_status,
                }))

        return render(request, template_name='user/login.html', context={
            'message': message,
            'message_status': message_status,
        })
