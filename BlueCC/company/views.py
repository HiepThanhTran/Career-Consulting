from django.shortcuts import render


def company_list(request):
    return render(request, template_name='company/company_list.html')


def company_top(request):
    return render(request, template_name='company/company_top.html')


def company_detail(request):
    return render(request, template_name='company/company_detail.html')
