from django.core.validators import EmailValidator

from apps.base.exceptions import CustomExceptionError
from apps.users.validators import phone_validate


def check_username_type(username):
    """Checking username type email or phone number"""
    validate_email = EmailValidator()

    try:
        phone_validate(username)
        username_type = 'phone_number'
    except CustomExceptionError:
        try:
            validate_email(username)
        except:
            raise CustomExceptionError(code=400, detail="Invalid phone number or email address.")
        username_type = 'email'
    return username_type