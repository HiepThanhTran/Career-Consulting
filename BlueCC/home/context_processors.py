from django.core.exceptions import ObjectDoesNotExist

from home import location_list
from job.models import JobDescription


def context_processors(request):
    try:
        _user_email_verified = request.user.emailaddress_set.filter(primary=True, verified=True).exists()
    except (ObjectDoesNotExist, Exception):
        _user_email_verified = False

    return {
        'user_email_verified': _user_email_verified,
        'location_list': location_list,
        'work_form': JobDescription.WorkForm,
        'gender': JobDescription.Gender,
    }