from allauth.account.models import EmailAddress

from user.models import User
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.adapter import DefaultAccountAdapter


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = User.objects.filter(email=sociallogin.user.email).first()
        if user and not sociallogin.is_existing:
            sociallogin.connect(request, user)

        # user = sociallogin.user
        # if user.id:
        #     return
        # try:
        #     user = User.objects.get(email=user.email)
        # except ObjectDoesNotExist:
        #     return
        # else:
        #     sociallogin.state['process'] = 'connect'
        #     perform_login(request, user, 'none')

    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        user.full_name = f"{user.first_name} {user.last_name}"
        email = EmailAddress.objects.filter(user__email__exact=user.email).first()
        email.verified = False
        email.save()
        user.save()
        return user
