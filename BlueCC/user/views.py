from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from user.models import User
from django.views import View

from user.tokens import account_activation_token
from utils.utils import is_safe_url
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model


def send_email(request, user, to_email, **kwargs):
    mail_subject = kwargs['mail_subject']
    message = render_to_string(template_name=kwargs['template'], context={
        'user': user.full_name,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        message = kwargs['message_success']
        message_status = True
    else:
        message = kwargs['message_error']
        message_status = False

    return {
        'message': message,
        'message_status': message_status,
    }


class UserSignin(View):
    def get(self, request):
        return render(request, template_name='user/login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        policy_check = request.POST.get('policy_check', None)
        user = authenticate(request, email=email, password=password)

        if user and policy_check in ['policy_check']:
            login(request, user)

            redirect_to = request.POST.get('next', 'home')
            if is_safe_url(url=redirect_to, allowed_hosts=request.get_host()):
                return redirect(redirect_to)
        message = 'Vui lòng đồng ý với chính sách của chúng tôi!' if not policy_check else 'Email hoặc mật khẩu không chính xác!'

        return render(request, template_name='user/login.html', context={
            'message': message
        })


class UserSignout(View):
    def get(self, request):
        logout(request)
        return redirect('home')

    def post(self, request):
        pass


class UserRegister(View):
    def get(self, request):
        return render(request, template_name='user/signup.html')

    def post(self, request):
        full_name = request.POST['full_name'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()
        password_confirm = request.POST['confirm'].strip()
        policy_check = request.POST.get('policy_check', None)

        message = 'Mật khẩu không khớp!' if not password == password_confirm else \
            'Vui lòng đồng ý với chính sách của chúng tôi!' if policy_check not in ['policy_check'] else None
        message_status = False

        if password == password_confirm and policy_check in ['policy_check']:
            user = User.objects.create_user(full_name=full_name, email=email, password=password)
            mail_result = send_email(request,
                                     user=user,
                                     to_email=email,
                                     mail_subject='Activate your user account',
                                     template='user/mail/template_activate_account.html',
                                     message_success='Email xác nhận được gửi vào hàm thư của bạn. Hãy nhấn vào link xác nhận và hoàn thành'
                                                     'quá trình đăng ký!',
                                     message_error='Gặp lỗi trong quá trình gửi mail xác nhận, vui lòng kiểm tra lại email của bạn!')

            message = mail_result['message']
            message_status = mail_result['message_status']

        return render(request, template_name='user/signup.html', context={
            'message': message,
            'message_status': message_status,
        })


class Activate(View):
    def get(self, request, uidb64=None, token=None):
        user = get_user_model()
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = user.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, user.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            # ...
            # user.save()
            message_status = True
            message = 'Xác nhận email thành công. Bạn có thể đăng nhập ngay bây giờ!'
        else:
            message_status = False
            message = 'Link xác nhận không hợp lệ!'

        return render(request, template_name='user/login.html', context={
            'message': message,
            'message_status': message_status,
        })


class UserPasswordReset(View):
    def get(self, request):
        return render(request, template_name='user/password_reset.html')

    def post(self, request):
        email = request.POST['email']
        policy_check = request.POST.get('policy_check', None)

        user = User.objects.filter(email=email).first()

        message = 'Tài khoản không tồn tại!' if not user else\
            'Vui lòng đồng ý với chính sách của chúng tôi!' if policy_check not in ['policy_check'] else None
        message_status = False

        if user and policy_check in ['policy_check']:
            mail_result = send_email(request,
                                     user=user,
                                     to_email=email,
                                     mail_subject='Password reset',
                                     template='user/mail/template_password_reset.html',
                                     message_success='Đã gửi yêu cầu thay đổi mật khẩu đến email của bạn!',
                                     message_error='Gặp lỗi trong quá trình gửi mail xác nhận, vui lòng kiểm tra lại email của bạn!')

            message = mail_result['message']
            message_status = mail_result['message_status']

        return render(request, template_name='user/password_reset.html', context={
            'message': message,
            'message_status': message_status,
        })


class PasswordSet(View):
    pass
