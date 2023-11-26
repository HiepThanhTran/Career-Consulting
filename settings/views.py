from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from home.models import Account
from settings.forms import UploadAvatarForm
import cloudinary.uploader


class ChangePassword(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, template_name='settings/password_change.html')

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
    def get(self, request):
        if request.user.has_perm('company.view_company') and not request.user.is_superuser:
            redirect_to = request.path
            login_url = reverse('login')
            message = 'Vui lòng đăng nhập vào tài khoản người dùng bình thường'
            return redirect(f'{login_url}?next={redirect_to}&message={message}')

        return render(request, template_name='settings/job_settings.html')

    def post(self, request):
        pass


class ProfileSettings(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.has_perm('company.view_company') and not request.user.is_superuser:
            redirect_to = request.path
            login_url = reverse('login')
            message = 'Vui lòng đăng nhập vào tài khoản người dùng bình thường'
            return redirect(f'{login_url}?next={redirect_to}&message={message}')

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

        account = Account.objects.filter(phone_number=data['phone_number']).first()

        if data['phone_number'] and account:
            return render(request, template_name='settings/profile_settings.html', context={
                'message': 'Số điện thoại đã được liên kết với tài khoản khác',
                'form': form,
                'message_status': False,
            })

        for field_name, field_value in data.items():
            if field_value:
                if field_name == 'full_name':
                    request.user.user.full_name = field_value
                    request.user.user.save()
                elif field_name == 'avatar':
                    path = cloudinary.uploader.upload(field_value)
                    request.user.avatar = path['secure_url']
                    request.user.save()
                else:
                    setattr(request.user, field_name, field_value)

        request.user.save()

        message = 'Cập nhật thông tin thành công!'

        return render(request, template_name='settings/profile_settings.html', context={
            'message': message,
            'form': form,
            'message_status': True,
        })
