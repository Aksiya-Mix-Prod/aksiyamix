import re

from django.core.exceptions import ValidationError
from django.core.validators import validate_image_file_extension
from PIL import Image

from apps.base.exceptions import CustomExceptionError


def validate_image_size(image, max_width, max_height, error_message):
    """ Validate image size """

    if not image:
        raise CustomExceptionError(code=400, detail="Provided file is not an image.")

    try:
        validate_image_file_extension(image)

        img = Image.open(image)
        if img.width > max_width or img.height > max_height:
            raise ValidationError(error_message)

    except (AttributeError, IOError):
        raise CustomExceptionError(code=400, detail="Invalid image file. Could not open the image.")



def validate_youtube_url(value):
    # ======== Regex pattern for YouTube URLs (includes both youtu.be and youtube.com variants) ========
    youtube_regex = re.compile(
        r'^(https?://)?(www\.)?((youtube\.com|youtu\.be)/.+)$'
    )
    if not youtube_regex.match(value):
        raise ValidationError('Invalid YouTube URL')
