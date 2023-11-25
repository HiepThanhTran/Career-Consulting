from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from settings.forms import UploadAvatarForm
from user.models import User


class ChangePassword(LoginRequiredMixin, View):
    def get(self, request, slug=None):
        user = User.objects.get(slug=slug)

        return render(request, template_name='settings/password_change.html', context={
            'user': user,
        })

    def post(self, request):
        old_password = request.POST.get('old_password', None)
        new_password = request.POST['new_password'].strip()
        new_password_confirm = request.POST['new_password_confirm'].strip()

        message_status = False

        if new_password == new_password_confirm:
            if not request.user.has_usable_password() or request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                message_status = True
                message = 'Thay đổi mật khẩu thành công!' if request.user.has_usable_password() else 'Đặt mật khẩu thành công!'
            else:
                message = 'Mật khẩu hiện tại không chính xác!'
        else:
            message = 'Mật khẩu không khớp!'

        return render(request=request, template_name='settings/password_change.html', context={
            'message': message,
            'message_status': message_status,
        })


class JobSettings(LoginRequiredMixin, View):
    def get(self, request, slug=None):
        if request.user.has_perm('company.view_company'):
            redirect_to = request.path
            login_url = reverse('login')
            message = 'Vui lòng đăng nhập vào tài khoản người dùng bình thường'
            return redirect(f'{login_url}?next={redirect_to}&message={message}')

        user = User.objects.get(slug=slug)

        return render(request, template_name='settings/job_settings.html', context={
            'user': user,
        })

    def post(self, request):
        pass


class ProfileSettings(LoginRequiredMixin, View):
    def get(self, request, slug=None):
        if request.user.has_perm('company.view_company'):
            redirect_to = request.path
            login_url = reverse('login')
            message = 'Vui lòng đăng nhập vào tài khoản người dùng bình thường'
            return redirect(f'{login_url}?next={redirect_to}&message={message}')

        user = User.objects.get(slug=slug)

        form = UploadAvatarForm()

        return render(request, template_name='settings/profile_settings.html', context={
            'form': form,
            'user': user,
        })

    def post(self, request):
        form = UploadAvatarForm()

        data = {
            'full_name': request.POST.get('full_name', None),
            'phone_number': request.POST.get('phone_number', None),
            'avatar': request.FILES.get('avatar', None),
        }

        for field_name, field_value in data.items():
            if field_value:
                if field_name == 'full_name':
                    request.user.user.full_name = field_value
                    request.user.user.save()
                setattr(request.user, field_name, field_value)

        request.user.save()

        message = 'Cập nhật thông tin thành công!'

        return render(request, template_name='settings/profile_settings.html', context={
            'message': message,
            'form': form,
        })
