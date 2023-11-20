from django.shortcuts import render
from django.views import View


class Home(View):
    def get(self, request):
        return render(request, template_name='home/index.html')

    def post(self, request):
        pass
