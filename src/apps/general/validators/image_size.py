from PIL import Image
from django.core.exceptions import ValidationError
from django.core.validators import validate_image_file_extension

def validate_image_size(image, max_width, max_height, error_message):
    """ Validate image size """
    if not image:
        raise ValidationError("Provided file is not an image.")

    try:
        validate_image_file_extension(image)

        img = Image.open(image)
        if img.width > max_width or img.height > max_height:
            raise ValidationError(error_message)

    except (AttributeError, IOError):
        raise ValidationError("Invalid image file. Could not open the image.")
