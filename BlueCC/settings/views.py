from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from settings.forms import UploadAvatarForm


class ChangePassword(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, template_name='settings/password_change.html')

    def post(self, request):
        message_status = False
        old_password = request.POST.get('old_password', None)
        new_password = request.POST['new_password'].strip()
        new_password_confirm = request.POST['new_password_confirm'].strip()

        if new_password == new_password_confirm:
            if not request.user.has_usable_password() or request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                message_status = True
                message = 'Thay đổi mật khẩu thành công!' if request.user.has_usable_password() else 'Đặt mật khẩu thành công!'
            else:
                message = 'Mật khẩu không hợp lệ!'
        else:
            message = 'Mật khẩu không khớp!'

        return render(request=request, template_name='settings/password_change.html', context={
            'message': message,
            'message_status': message_status,
        })


class JobSettings(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, template_name='settings/job_settings.html')

    def post(self, request):
        pass


class ProfileSettings(LoginRequiredMixin, View):
    def get(self, request):
        form = UploadAvatarForm()

        return render(request, template_name='settings/profile_settings.html', context={
            'form': form
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
