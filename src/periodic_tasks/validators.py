from croniter import croniter
from django.utils import timezone

from django.core.exceptions import ValidationError


def validate_crontab_string(value):
    if not value:
        return True
    try:
        croniter(value, timezone.now())
    except Exception:
        raise ValidationError(
            '%(value)s is not a valid crontab string',
            params={'value': value},
        )
