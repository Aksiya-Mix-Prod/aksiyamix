from apps.base.exceptions import CustomExceptionError
from django.utils.translation import gettext_lazy as _
from PIL import Image

COMPANY_LOGO_MAX_SIZE = 1024 * 1024 * 30
COMPANY_ICON_MAX_SIZE = 1024 * 1024 * 20


def validate_company_logo_size(value):
    """
    Here checking logo size, MAX SIZE OF LOGO 30 MB
    """

    if value.size > COMPANY_LOGO_MAX_SIZE:
        raise CustomExceptionError(_("The logo size cannot be larger than 30 MB."))


def validate_logo_size(logo):
    """
    Custom validator to check the upload logo
    """
    img = Image.open(logo)
    max_width = 3000
    max_height = 1500

    if img.width > max_width or img.height > max_height:
        raise CustomExceptionError(
            _("The logo dimensions must be less than or equal to 3000x1500 pixels.")
        )


def validate_icon_size(icon):
    """
    Custom validator to check the upload icon
    """
    img = Image.open(icon)
    max_width = 300
    max_height = 150

    if img.width > max_width or img.height > max_height:
        raise CustomExceptionError(
            _("The icon dimensions must be less than or equal to 300x150 pixels.")
        )
