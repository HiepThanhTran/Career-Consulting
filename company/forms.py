from django import forms

from company.models import Company
from job.models import JobDescription
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CompanySettingsForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'input',
                'id': 'company_name',
                'placeholder': 'Tên công ty',
            }),
            'description': forms.TextInput(attrs={
                'class': 'textarea',
                'id': 'company_description',
                'placeholder': 'Mô tả công ty',
            }),
            'address': forms.TextInput(attrs={
                'class': 'input',
                'id': 'address',
                'placeholder': 'Địa chỉ công ty',
            }),
            'number_of_employees': forms.NumberInput(attrs={
                'class': 'input',
                'id': 'number_of_employees',
                'placeholder': 'Số lượng nhân viên',
            }),
            'social_link': forms.TextInput(attrs={
                'class': 'input',
                'id': 'social_link',
                'placeholder': 'Liên kết mạng xã hội',
            }),
            'industry': forms.TextInput(attrs={
                'class': 'input',
                'id': 'industry',
                'placeholder': 'Lĩnh vực',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ''


class UploadRecruitmentForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    requirements = forms.CharField(widget=CKEditorUploadingWidget)
    benefits = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = JobDescription
        fields = ['name', 'salary_start', 'salary_end', 'location', 'deadline',
                  'description', 'requirements', 'benefits', 'position',
                  'experience_year', 'number_of_recruits', 'work_form', 'gender']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input',
                'id': 'input',
                'style': 'padding: 12px;',
                'placeholder': 'Tiêu đề',
            }),
            'salary_start': forms.NumberInput(attrs={
                'class': 'input-cal input-base',
                'id': 'input',
                'style': 'width: auto;',
            }),
            'salary_end': forms.NumberInput(attrs={
                'class': 'input-cal input-base',
                'id': 'input',
                'style': 'width: 100%;',
            }),
            'location': forms.TextInput(attrs={
                'class': 'input-cal input-base',
                'id': 'input',
            }),
            'experience_year': forms.NumberInput(attrs={
                'class': 'input-cal input-base',
                'id': 'input',
            }),
            'description': forms.Textarea(attrs={
                'class': 'input-cal input-base',
                'id': 'input',
                'required': 'required',
            }),
            'requirements': forms.Textarea(attrs={
                'class': 'input-cal input-base',
                'id': 'input',
                'required': 'required',
            }),
            'benefits': forms.Textarea(attrs={
                'class': 'input-cal input-base',
                'id': 'input',
                'required': 'required',
            }),
            'deadline': forms.DateInput(attrs={
                'class': 'input-date',
                'type': 'date',
            }),
            'position': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Cấp bậc',
            }),
            'number_of_recruits': forms.NumberInput(attrs={
                'class': 'input',
                'placeholder': 'Số lượng người cần tuyển',
            }),
            'work_form': forms.Select(attrs={
                'class': 'input',
                'placeholder': 'Hình thức làm việc',
            }),
            'gender': forms.Select(attrs={
                'class': 'input',
                'placeholder': 'Giới tính',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(UploadRecruitmentForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ''
