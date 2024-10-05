from PIL import Image

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


COMPANY_BANNER_MAX_SIZE = 1024 * 1024 * 10


def validate_company_banner_size(value):
    """
    Here checking banner size, MAX SIZE OF BANNER 10 MB
    """

    if value.size > COMPANY_BANNER_MAX_SIZE:
        raise ValidationError(_('The banner size cannot be larger than 10 MB.'))


def validate_banner_size(banner):
    """
    Custom validator to check the upload banner
    """
    poster = Image.open(banner)

    max_width = 1000
    max_height = 500

    if poster.width > max_width or poster.height > max_height:
        raise ValidationError(_('The banner dimensions must be less than or equal to 1000x500 pixels.'))
