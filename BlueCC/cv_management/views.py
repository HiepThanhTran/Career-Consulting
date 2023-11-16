from django.shortcuts import render, redirect


def cv_major(request):
    return render(request, template_name='cv_management/cv_major.html')


def cv_management(request):
    if not request.user.is_authenticated:
        return redirect('sign-in')

    return render(request, template_name='cv_management/cv_management.html')


def cv_template(request):
    return render(request, template_name='cv_management/cv_template.html')
