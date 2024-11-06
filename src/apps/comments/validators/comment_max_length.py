import os

from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from rest_framework.exceptions import ValidationError

# from profanity_check import predict, predict_prob

@deconstructible
class CommentValidator(BaseValidator):
    """
    This class handles all comment-related validations, including length, content restrictions,
    and other business rules.
    """
    def __call__(self, value):
        """
        Main method to validate the comment based on multiple criteria such as
        length and any other custom rules.

        @param value: The comment string to be validated.
        @raises serializers.ValidationError: If any validation rule is violated.
        """
        self.validate_length(value)
        # self.validate_forbidden_words(value)

    def validate_length(self, value):
        """
        Ensures the comment does not exceed the maximum allowed length.
        """
        if len(value) > self.limit_value:
            raise ValidationError(f'Comment must be no longer than {self.limit_value} characters.')

    # def validate_forbidden_words(self, value):
    #     """
    #     Ensures the comment does not contain forbidden or inappropriate words.
    #     Uses profanity_check model rules to determine if a word is forbidden.
    #
    #     Doc: https://pypi.org/project/profanity-check/
    #     """
    #     # ======== predict() takes an array and returns a 1 for each string if it is offensive, else 0. ========
    #     forbidden_words = predict([value])
    #     if any(forbidden_words):
    #         raise serializers.ValidationError(f'Comment contains forbidden or inappropriate words.')
    #
    #     # ==== predict_prob() takes an array and returns the probability each string is offensive (# [0.08686173]) ====
    #     forbidden_words_probability = predict_prob([value])
    #     if forbidden_words_probability[0] > 0.5:
    #         raise serializers.ValidationError(f'Comment contains forbidden or inappropriate words.')
