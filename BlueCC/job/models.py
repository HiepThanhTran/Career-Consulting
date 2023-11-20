from django.db import models
from accounts.models import User
from company.models import Company
from ckeditor.fields import RichTextField


class JobDescription(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jds')
    users = models.ManyToManyField(User, related_name='jobs', through='JobApplication')
    name = models.CharField(max_length=50, null=False)
    wage_start = models.IntegerField(null=False)
    wage_end = models.IntegerField(null=False)
    location = models.CharField(max_length=50, null=False)
    deadline = models.DateField(null=False)
    description = RichTextField()
    requirements = RichTextField()
    benefits = RichTextField()
    position = models.CharField(max_length=50, null=False)
    experience_year = models.CharField(max_length=20, null=False)
    number_of_recruits = models.IntegerField(null=True)
    work_form = models.CharField(max_length=20, null=False)
    gender = models.CharField(max_length=20, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
