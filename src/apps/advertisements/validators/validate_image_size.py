from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image


def validate_image_size(image):
    """
    Here Checking image size
    """
    if image.size > 10 * 1024 * 1024:  # 10MB
        raise ValidationError(_("The image size should not exceed 10MB."))


def validate_image_resize(image):
    """
    Here Resize of image
    """

    image = Image.open(image)

    max_width = 1000
    max_height = 500

    if image.width > max_width or image.height > max_height:
        raise ValidationError(_('The banner dimensions must be less than or equal to 1000x500 pixels.'))

