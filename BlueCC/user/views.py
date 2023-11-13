from django.shortcuts import render


def user_login(request):
    return render(request, template_name='user/login.html')


def user_register(request):
    return render(request, template_name='user/register.html')


def user_forgot_password(request):
    return render(request, template_name='user/forgot_password.html')
