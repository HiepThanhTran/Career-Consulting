from django.db import models
from .manages import CustomUserManager
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None

    full_name = models.CharField(max_length=50, null=False)
    gender = models.BooleanField(null=True, blank=True)
    email = models.EmailField(null=False, unique=True)
    phone_number = models.IntegerField(null=True, blank=True, unique=True)
    password = models.CharField(max_length=100, null=False)
    avatar = models.ImageField(upload_to='upload/%Y/%m')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name

    def get_username(self):
        return self.full_name
