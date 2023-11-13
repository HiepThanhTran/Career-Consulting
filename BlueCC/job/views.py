from django.shortcuts import render


def suitable_job(request):
    return render(request, template_name='job/suitable_job.html')


def applied_job(request):
    return render(request, template_name='job/applied_job.html')


def saved_job(request):
    return render(request, template_name='job/saved_job.html')


def search_job(request):
    return render(request, template_name='job/search_job.html')
