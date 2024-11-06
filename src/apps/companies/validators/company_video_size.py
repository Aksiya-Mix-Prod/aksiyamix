from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

COMPANY_VIDEO_MAX_SIZE = 1024 * 1024 * 15


def validate_company_video_size(value):
    """
    Here checking video size, MAX SIZE OF VIDE 15 MB
    """

    if value.size > COMPANY_VIDEO_MAX_SIZE:
        raise ValidationError(_('The video size cannot be larger than 15 MB.'))

