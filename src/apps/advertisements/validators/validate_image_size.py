from apps.base.exceptions import CustomExceptionError
from django.utils.translation import gettext_lazy as _
from PIL import Image


def validate_image_size_of_advertisements(image):
    """Check if image size exceeds the limit (e.g., 10 MB)."""
    if image.size > 10 * 1024 * 1024:  # 10 MB limit
        raise CustomExceptionError(_("The image size should not exceed 10MB."))


def validate_image_resize_of_advertisements(image):
    """Check if image dimensions exceed the maximum allowed size."""
    img = Image.open(image)
    max_width, max_height = 1000, 500
    if img.width > max_width or img.height > max_height:
        raise CustomExceptionError(
            _("The image dimensions must be less than or equal to 1000x500 pixels.")
        )
