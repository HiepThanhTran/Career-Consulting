from urllib.parse import urlparse

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from user.tokens import account_activation_token


def is_safe_url(url, allowed_hosts):
    url_info = urlparse(url)
    return url_info.netloc in allowed_hosts


def send_email_reset_password(request, account, to_email, **kwargs):
    mail_subject = kwargs['mail_subject']
    message = render_to_string(template_name=kwargs['template'], context={
        'user': account.user__set.full_name,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(account.pk)),
        'token': account_activation_token.make_token(account),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        message = kwargs['message_success']
        message_status = True
    else:
        message = 'Gặp lỗi trong quá trình gửi mail xác nhận, vui lòng kiểm tra lại email của bạn!'
        message_status = False

    return {
        'message': message,
        'message_status': message_status,
    }
