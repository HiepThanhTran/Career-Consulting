from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from user.models import User


def user_signin(request):
    error_msg = ''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        policy_check = request.POST.get('policy_check', None)
        user = authenticate(request, email=email, password=password)

        if user and policy_check in ['policy_check']:
            login(request, user)
            return redirect('home')
        error_msg = 'Vui lòng đồng ý với chính sách của chúng tôi!' if not policy_check else 'Tên người dùng hoặc mật khẩu không chính xác!'

    return render(request, template_name='user/login.html', context={
        'error_msg': error_msg,
    })


def user_signout(request):
    logout(request)
    return redirect('home')


def user_register(request):
    error_msg = ''
    if request.method == 'POST':
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

    return render(request, template_name='user/register.html', context={
        'error_msg': error_msg,
    })


def user_forgot_password(request):
    return render(request, template_name='user/forgot_password.html')
