from django.contrib.auth.models import AbstractUser
from django.db import models

from django.dispatch import receiver
from allauth.account.models import EmailAddress
from allauth.account.signals import user_signed_up

from home.manages import CustomUserManager


@receiver(user_signed_up)
def user_signed_up_(request, account, sociallogin=None, **kwargs):
    preferred_avatar_size_pixels = 256

    if sociallogin:
        if sociallogin.account.provider == 'google':
            email_address = EmailAddress.objects.filter(email=account.email).first()
            email_address.send_confirmation(request)

        if sociallogin.account.provider == 'facebook':
            picture_url = "https://graph.facebook.com/{0}/picture?width={1}&height={1}".format(
                sociallogin.account.uid, preferred_avatar_size_pixels)

            account.avatar = picture_url
            account.save()


class Account(AbstractUser):
    phone_number = models.IntegerField(null=True, blank=True, unique=True)
    avatar = models.ImageField(upload_to='upload/avatar/%Y/%m', null=True, blank=True)

    objects = CustomUserManager()
