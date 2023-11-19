from django.db import models
from utils.manages import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = None
    full_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=100, null=False)
    phone_number = models.IntegerField(null=True, blank=True, unique=True)
    avatar = models.ImageField(upload_to='upload/%Y/%m', null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['full_name']

    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
    ]

    gender = models.BooleanField(null=True, blank=True, choices=GENDER_CHOICES)

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name

    def get_username(self):
        return self.full_name
