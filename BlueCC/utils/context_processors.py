from django.shortcuts import redirect
from django.templatetags.static import static


def avatar_context(request):
    if request.user.is_authenticated:
        if request.user.avatar:
            avatar_url = static('images/' + str(request.user.avatar))
        else:
            avatar_url = static('images/default-avatar.jpg')
    else:
        avatar_url = static('images/default-avatar.jpg')

    return {'avatar_url': avatar_url}

