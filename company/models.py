from django.db import models
from ckeditor.fields import RichTextField

from home.models import Account


class Company(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=50, null=False, unique=True)
    description = RichTextField()
    address = models.CharField(max_length=100, null=True)
    number_of_employees = models.IntegerField(null=True, default=0)
    social_link = models.CharField(max_length=254, null=True)
    industry = models.CharField(max_length=50, null=True)
    followers = models.IntegerField(default=0)

    def __str__(self):
        return self.company_name
