from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, REDIRECT_FIELD_NAME
from django.views import View
from user.models import User
from utils.utils import is_safe_url


class UserSignin(View):
    def get(self, request, error_msg=''):
        return render(request, template_name='user/login.html', context={
            'error_msg': error_msg,
        })

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        policy_check = request.POST.get('policy_check', None)
        user = authenticate(request, email=email, password=password)

        if user and policy_check in ['policy_check']:
            login(request, user)

            redirect_to = request.POST.get('next')
            if is_safe_url(url=redirect_to, allowed_hosts=request.get_host()):
                return redirect(redirect_to)
            return redirect('home')
        error_msg = 'Vui lòng đồng ý với chính sách của chúng tôi!' if not policy_check else 'Tên người dùng hoặc mật khẩu không chính xác!'

        return self.get(request=request, error_msg=error_msg)


class UserSignout(View):
    def get(self, request):
        logout(request)
        return redirect('home')

    def post(self, request):
        pass


class UserRegister(View):
    def get(self, request, error_msg=''):
        return render(request, template_name='user/register.html', context={
            'error_msg': error_msg,
        })

    def post(self, request):
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']
        policy_check = request.POST.get('policy_check', None)

        if password.strip().__eq__(confirm.strip()) and policy_check in ['policy_check']:
            User.objects.create_user(full_name=full_name, email=email, password=password)
            return redirect('sign-in')
        error_msg = 'Mật khẩu không khớp!' if not password.strip().__eq__(
            confirm.strip()) else 'Vui lòng đồng ý với chính sách của chúng tôi!'

        return self.get(request=request, error_msg=error_msg)


class UserForgotPassword(View):
    def get(self, request):
        return render(request, template_name='user/forgot_password.html')

    def post(self, request):
        pass
