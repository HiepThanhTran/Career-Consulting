from django.shortcuts import render


def change_password(request):
    return render(request, template_name='settings/change_password.html')


def job_settings(request):
    return render(request, template_name='settings/job_settings.html')


def profile_settings(request):
    return render(request, template_name='settings/profile_settings.html')
