from django.db import models
from ckeditor.fields import RichTextField


class Company(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    description = RichTextField()
    address = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False, unique=True)
    phone_number = models.IntegerField(null=False, unique=True)
    number_of_employees = models.IntegerField(null=False)
    avatar = models.ImageField(upload_to='upload/%Y/%m')
    social_link = models.CharField(max_length=254, null=True)
    industry = models.CharField(max_length=50, null=False)
    followers = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
