from django.core.exceptions import ObjectDoesNotExist

from utils import location_list


def user_email_verified(request):
    if request.user.is_authenticated:
        _user_email_verified = request.user.emailaddress_set.filter(primary=True, verified=True).exists()
        return {'user_email_verified': _user_email_verified}

    return {'user_email_verified': False}


def location_context(request):
    return {'location_list': location_list}
