from django.core.exceptions import ValidationError

def year_validator(value):
    if int(value) < 1999 or int(value) > 2030:
        raise ValidationError("Year must be between 1999 and 2030!")