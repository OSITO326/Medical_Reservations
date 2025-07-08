from django.core.exceptions import ValidationError
import re


# def only_letters(value):
#     if not re.match(r'^[A-Za-z ]+$', value):
#         raise ValidationError('Only letters are allowed.')
## only_letters include áéíóúñ
def only_letters(value):
    if not re.match(r'^[A-Za-záéíóúñÁÉÍÓÚÑ ]+$', value):
        raise ValidationError(
            'Only letters are allowed, including accented characters.'
        )


def email_validator(value):
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
        raise ValidationError('Invalid email format.')
