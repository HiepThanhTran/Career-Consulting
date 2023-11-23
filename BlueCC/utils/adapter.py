from allauth.account.models import EmailAddress
from allauth.account.utils import perform_login
from django.core.exceptions import ObjectDoesNotExist

from home.models import Account
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = Account.objects.filter(email=sociallogin.account.email).first()
        if user and not sociallogin.is_existing:
            sociallogin.connect(request, user)

        user = sociallogin.user
        if user.id:
            return
        try:
            user = Account.objects.get(email=user.email)
        except ObjectDoesNotExist:
            return
        else:
            sociallogin.state['process'] = 'connect'
            perform_login(request, user, 'none')

    def save_user(self, request, sociallogin, form=None):
        account = super().save_user(request, sociallogin, form)
        account.name = f"{account.first_name} {account.last_name}"
        account.save()
        email = EmailAddress.objects.filter(user__email__exact=account.email).first()
        email.verified = False
        email.save()
        return account
