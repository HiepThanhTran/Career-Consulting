from django.db import models
from user.models import User
from company.models import Company
from ckeditor.fields import RichTextField


class JobDescription(models.Model):
    class Gender(models.TextChoices):
        MALE = 'Nam'
        FEMALE = 'Nữ'
        BOTH = 'Cả hai'
        UNKNOWN = 'Không yêu cầu'

    class WorkForm(models.TextChoices):
        PART_TIME = 'Bán thời gian'
        FULL_TIME = 'Toàn thời gian'
        BOTH = 'Cả hai'

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jds')
    users = models.ManyToManyField(User, related_name='jobs', through='JobApplication')
    name = models.CharField(max_length=50, null=False)
    salary_start = models.IntegerField(null=False)
    salary_end = models.IntegerField(null=False)
    location = models.CharField(max_length=50, null=False)
    deadline = models.DateField(null=False)
    description = RichTextField()
    requirements = RichTextField()
    benefits = RichTextField()
    position = models.CharField(max_length=50, null=False)
    experience_year = models.CharField(max_length=20, null=False)
    number_of_recruits = models.IntegerField(null=True)
    work_form = models.CharField(max_length=20, null=False, choices=[(work.name, work.value) for work in WorkForm])
    gender = models.CharField(max_length=20, null=True, choices=[(gender.name, gender.value) for gender in Gender])
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class JobApplication(models.Model):
    class Meta:
        unique_together = ['user', 'job']

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
