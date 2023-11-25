from django import template
from dateutil.relativedelta import relativedelta
from datetime import datetime
from django.utils import timezone

register = template.Library()


@register.filter
def days_until(deadline):
    delta = deadline - datetime.now().date()
    return delta.days


@register.filter
def hours_since_updated(updated_date):
    now = timezone.now()
    delta = now - updated_date

    if delta.total_seconds() < 0:
        return "Mới đây"
    elif delta.total_seconds() < 60:
        return f"Cập nhật {round(delta.total_seconds())} giây trước"
    elif delta.total_seconds() < 3600:
        return f"Cập nhật {round(delta.total_seconds() / 60)} phút trước"
    elif delta.total_seconds() < 86400:
        return f"Cập nhật {round(delta.total_seconds() / 3600)} giờ trước"
    else:
        diff = relativedelta(now, updated_date)

        if diff.years > 0:
            return f"Cập nhật {diff.years} năm trước"
        elif diff.months > 0:
            return f"Cập nhật {diff.months} tháng trước"
        else:
            return f"Cập nhật {diff.days} ngày trước"

