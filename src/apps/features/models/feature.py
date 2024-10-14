from django.db import models

from src.apps.base.models import AbstractBaseModel


class Feature(AbstractBaseModel):
    """
    Model to create feature
    """

    # to which category
    category = models.ForeignKey('categories.Category', on_delete=models.PROTECT)

    # measure of feature
    measure = models.CharField(max_length=100, blank=True)

    # name information
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        db_table = "feature"
        unique_together = (('category', 'slug'),)


class FeatureValue(AbstractBaseModel):
    """
    Model to add feature value to feature
    """

    # from which feature
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='children')

    # which value
    value = models.CharField(max_length=255)

    class Meta:
        db_table = "feature_value"

