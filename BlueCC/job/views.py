from django.shortcuts import render
from django.views import View


class SuitableJob(View):
    def get(self, request):
        return render(request, template_name='job/suitable_job.html')

    def post(self, request):
        pass


class AppliedJob(View):
    def get(self, request):
        return render(request, template_name='job/applied_job.html')

    def post(self, request):
        pass


class SavedJob(View):
    def get(self, request):
        return render(request, template_name='job/saved_job.html')

    def post(self, request):
        pass


class SearchJob(View):
    def get(self, request):
        return render(request, template_name='job/search_job.html')

    def post(self, request):
        pass
