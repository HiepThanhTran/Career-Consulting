from allauth.account.signals import email_confirmed, user_signed_up
from django.contrib.auth import login
from django.db import models
from django.dispatch import receiver

from utils.manages import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


@receiver(email_confirmed)
def email_confirmed_(request, email_address, **kwargs):
    user = User.objects.filter(email__iexact=email_address.email).first()
    user.is_verified = True
    user.save()


@receiver(user_signed_up)
def user_signed_up_(request, user, sociallogin=None, **kwargs):
    if sociallogin:
        login(request, user, backend='allauth.account.auth_backends.AuthenticationBackend')


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
