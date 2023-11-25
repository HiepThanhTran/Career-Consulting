from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.models import EmailAddress
from allauth.account.utils import perform_login
from django.core.exceptions import ObjectDoesNotExist

from home.models import Account
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from user.models import User


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        path = "/account/login/"
        return path


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        account = sociallogin.user
        if account.id:
            return
        try:
            account = Account.objects.get(email=account.email)
        except ObjectDoesNotExist:
            return
        else:
            sociallogin.state['process'] = 'connect'
            perform_login(request, account, 'none')

    def save_user(self, request, sociallogin, form=None):
        account = super().save_user(request, sociallogin, form)
        account.username = account.email
        account.save()
        user = User(account=account, full_name=f"{account.first_name} {account.last_name}")
        user.save()
        email = EmailAddress.objects.filter(user__email__exact=account.email).first()
        email.verified = False
        email.save()
        return account
