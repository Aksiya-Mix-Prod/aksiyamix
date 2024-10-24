from django.core.exceptions import ValidationError
import re

def validate_youtube_url(value):
    # ======== Regex pattern for YouTube URLs (includes both youtu.be and youtube.com variants) ========
    youtube_regex = re.compile(
        r'^(https?://)?(www\.)?((youtube\.com|youtu\.be)/.+)$'
    )
    if not youtube_regex.match(value):
        raise ValidationError('Invalid YouTube URL')
