from django.db import models

from home.models import Account
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('FEMALE')

    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.BooleanField(null=True, blank=True, choices=Gender.choices)

    @property
    def email(self):
        return self.account.email

    def __str__(self):
        return self.full_name
