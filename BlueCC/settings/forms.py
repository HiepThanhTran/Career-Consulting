from django import forms

from home.models import Account


class UploadAvatarForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['avatar']
        widgets = {
            'avatar': forms.FileInput(attrs={
                'class': 'input_avatar',
                'id': 'input_avatar',
                'accept': 'image/jpeg, image/png, image/jpg'
            })
        }
