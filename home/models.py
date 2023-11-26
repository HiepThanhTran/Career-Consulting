from django.contrib.auth.models import AbstractUser
from django.db import models

from django.dispatch import receiver
from allauth.account.models import EmailAddress
from allauth.account.signals import user_signed_up

from BlueCC.settings import DEFAULT_AVATAR
from home.manages import CustomUserManager


@receiver(user_signed_up)
def user_signed_up_(request, user, sociallogin=None, **kwargs):
    preferred_avatar_size_pixels = 256
    picture_url = DEFAULT_AVATAR

    if sociallogin:
        if sociallogin.account.provider == 'google':
            email_address = EmailAddress.objects.filter(email=user.email).first()
            email_address.send_confirmation(request)
            picture_url = sociallogin.account.extra_data['picture']

        if sociallogin.account.provider == 'facebook':
            picture_url = "https://graph.facebook.com/{0}/picture?width={1}&height={1}".format(
                sociallogin.account.uid, preferred_avatar_size_pixels)

    user.avatar = picture_url
    user.save()


class Account(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True, unique=True)
    avatar = models.CharField(max_length=254, null=True, blank=True, default=DEFAULT_AVATAR)

    objects = CustomUserManager()
