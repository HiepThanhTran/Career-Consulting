from allauth.account.models import EmailAddress
from allauth.account.signals import email_confirmed, user_signed_up
from django.contrib.auth import login
from django.db import models
from django.dispatch import receiver

from utils.manages import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


@receiver(user_signed_up)
def user_signed_up_(request, user, sociallogin=None, **kwargs):
    preferred_avatar_size_pixels = 256

    if sociallogin:
        if sociallogin.account.provider == 'google':
            email_address = EmailAddress.objects.filter(email=user.email).first()
            email_address.send_confirmation(request)

        if sociallogin.account.provider == 'facebook':
            picture_url = "https://graph.facebook.com/{0}/picture?width={1}&height={1}".format(
                sociallogin.account.uid, preferred_avatar_size_pixels)

            user.avatar = picture_url
            user.save()


class User(AbstractUser):
    username = None
    full_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=100, null=False)
    phone_number = models.IntegerField(null=True, blank=True, unique=True)
    avatar = models.ImageField(upload_to='upload/%Y/%m', null=True, blank=True, default='/static/images/default-avatar.jpg')

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
