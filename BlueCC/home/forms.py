from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from company.models import Company
from job.models import JobDescription


class CompanyForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Company
        fields = '__all__'


class JDForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    requirements = forms.CharField(widget=CKEditorUploadingWidget)
    benefits = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = JobDescription
        fields = '__all__'
