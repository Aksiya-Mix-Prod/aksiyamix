from apps.base.validators.validators import validate_image_size

def parent_category_icon_size(image):
    validate_image_size(image, 32, 32, "Category icon size should be 32x32")
