from django.db import models
from .manages import CustomUserManager
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    full_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=100, null=False)
    phone_number = models.IntegerField(null=True, blank=True, unique=True)
    gender = models.BooleanField(null=True, blank=True)
    avatar = models.ImageField(upload_to='upload/%Y/%m', null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name

    def get_username(self):
        return self.full_name
