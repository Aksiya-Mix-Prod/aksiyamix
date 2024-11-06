import os
import subprocess

from django.core.exceptions import ValidationError
from moviepy.editor import VideoFileClip


def discount_video_format(video):
    """ Validate Video format for the Discount """
    valid_video_extensions = ['.mp4', '.avi', '.mov', ]
    ext = os.path.splitext(video.name)[1]
    if ext.lower() not in valid_video_extensions:
        raise ValidationError("Unsupported file extension. Please upload a video in .mp4, .mov, or .avi format.")


def get_video_duration(video_path):
    """ Get video duration
    """
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", video_path],
        stdout=subprocess.PIPE, # get output
        stderr=subprocess.STDOUT, # get output
    )
    return float(result.stdout)

def validate_video_duration(video):
    """ Validate Company Vide Duration
    The video duration should not exceed 2 minutes
    """
    max_duration = 120 # 2 minutes
    duration = get_video_duration(video.file.path)
    if duration > max_duration:
        raise ValidationError("The video duration should not exceed 5 minutes")


def validate_video_resolution(video):
    """ Validate Company Video Resolution
    The video resolution should be up to 3840x2160 (4K UHD
    """
    max_width = 3840
    max_height = 2160
    clip = VideoFileClip(video.file.path)
    width, height = clip.size
    if width > max_width or height > max_height:
        raise ValidationError("The video resolution should be up to 3840x2160 (4K UHD)")

