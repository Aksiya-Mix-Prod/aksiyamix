from apps.general.validators.image_size import validate_image_size

def parent_category_image_size(image):
    validate_image_size(image, 500, 250, "Image size should be 500x250")
