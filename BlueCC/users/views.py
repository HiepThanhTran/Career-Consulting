from django.shortcuts import render
from django.http import HttpResponse


def user_login(request):
    return render(request, template_name='users/login.html')


def user_register(request):
    return render(request, template_name='users/register.html')


def user_forgot_password(request):
    return render(request, template_name='users/forgot_password.html')
