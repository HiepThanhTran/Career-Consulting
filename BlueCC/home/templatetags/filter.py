from datetime import datetime

from django import template
from django.utils import timezone

register = template.Library()


@register.filter
def days_until(deadline):
    delta = deadline - datetime.now().date()
    return delta.days


@register.filter()
def hours_since_updated(updated_date):
    delta = timezone.now() - updated_date

    if delta.total_seconds() < 0:
        return "Mới đây"
    elif delta.total_seconds() < 60:
        return f"Cập nhật {round(delta.total_seconds())} giây trước"
    elif delta.total_seconds() < 3600:
        return f"Cập nhật {round(delta.total_seconds() / 60)} phút trước"
    else:
        return f"Cập nhật {round(delta.total_seconds() / 3600)} giờ trước"
