from apps.base.validators.validators import validate_image_size

def discount_image_size(image):
    validate_image_size(image, 500, 500, "Image size should be 500x500")