from django.shortcuts import render
from django.views import View


class CompanyList(View):
    def get(self, request):
        return render(request, template_name='company/company_list.html')

    def post(self, request):
        pass


class CompanyTop(View):
    def get(self, request):
        return render(request, template_name='company/company_top.html')

    def post(self, request):
        pass


class CompanyDetail(View):
    def get(self, request):
        return render(request, template_name='company/company_detail.html')

    def post(self, request):
        pass

class CompanyLogin(View):
    def get(self, request):
        return render(request, template_name='company/login.html')

    def post(self, request):
        pass

class CompanySignUp(View):
    def get(self, request):
        return render(request, template_name='company/signup.html')

    def post(self, request):
        pass
