from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image

COMPANY_LOGO_MAX_SIZE = 1024 * 1024 * 10
COMPANY_ICON_MAX_SIZE = 1024 * 1024 * 5


def validate_company_logo_size(value):
    """
    Here checking logo size, MAX SIZE OF LOGO 10 MB
    """

    if value.size > COMPANY_LOGO_MAX_SIZE:
        raise ValidationError(_('The logo size cannot be larger than 10 MB.'))


def validate_logo_size(logo):
    """
    Custom validator to check the upload logo
    """
    img = Image.open(logo)
    max_width = 500
    max_height = 250

    if img.width > max_width or img.height > max_height:
        raise ValidationError(_('The logo dimensions must be less than or equal to 500x250 pixels.'))


def validate_icon_size(icon):
    """
    Custom validator to check the upload icon
    """
    img = Image.open(icon)
    max_width = 150
    max_height = 150

    if img.width > max_width or img.height > max_height:
        raise ValidationError(_('The icon dimensions must be less than or equal to 150x150 pixels.'))



