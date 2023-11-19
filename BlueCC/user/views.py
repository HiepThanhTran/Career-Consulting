from user.models import User
from django.views import View
from utils.utils import is_safe_url
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


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

            redirect_to = request.POST.get('next', 'home')
            if is_safe_url(url=redirect_to, allowed_hosts=request.get_host()):
                return redirect(redirect_to)
        error_msg = 'Vui lòng đồng ý với chính sách của chúng tôi!' if not policy_check else 'Email hoặc mật khẩu không chính xác!'

        return self.get(request=request, error_msg=error_msg)


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

        if password == password_confirm and policy_check in ['policy_check']:
            User.objects.create_user(full_name=full_name, email=email, password=password)
            return redirect('login')
        messages = 'Mật khẩu không khớp!' if not password == password_confirm else 'Vui lòng đồng ý với chính sách của chúng tôi!'

        return render(request, template_name='user/signup.html', context={
            'messages': messages,
        })


class UserPasswordReset(View):
    def get(self, request):
        return render(request, template_name='user/password_reset.html')

    def post(self, request):
        pass
