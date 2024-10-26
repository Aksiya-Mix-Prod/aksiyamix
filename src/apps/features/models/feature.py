from django.db import models
from django.utils.text import slugify

from apps.base.exceptions import CustomExceptionError
from apps.base.models import AbstractBaseModel


class Feature(AbstractBaseModel):
    """
    Feature Model
    """

    category = models.ForeignKey(
        to='categories.Category',
        on_delete=models.PROTECT,
        limit_choices_to={'parent__parent__isnull': False},
        help_text='to which category'
    )

    measure = models.CharField(max_length=100, blank=True, help_text='measure of feature')

    is_active = models.BooleanField(default=False)

    ordering = models.PositiveSmallIntegerField(help_text='order of feature')

    name = models.CharField(max_length=255, help_text='name')
    slug = models.SlugField(max_length=255, editable=False)

    def clean(self):
        self.slug = slugify(self.name)
        if Feature.objects.filter(category_id=self.category_id, slug=self.slug).exists():
            raise CustomExceptionError(code=400, detail={'name': 'this feature has already exists'})

    class Meta:
        db_table = "feature"
        unique_together = (('category', 'slug'),)


class FeatureValue(AbstractBaseModel):
    """
    Feature Value Model
    """

    feature = models.ForeignKey(
        to=Feature,
        on_delete=models.PROTECT,
        related_name='children',
        help_text='from which feature'
    )

    value = models.CharField(max_length=255, help_text='which value')
    slug = models.SlugField(max_length=255, editable=False)

    is_active = models.BooleanField(default=False)

    ordering = models.PositiveSmallIntegerField(help_text='order of feature values')

    def clean(self):
        self.slug = slugify(self.value)
        if Feature.objects.filter(feature_id=self.feature_id, slug=self.slug).exists():
            raise CustomExceptionError(code=400, detail={'value': 'feature value in this feature has already exists'})

    class Meta:
        db_table = "feature_value"
        unique_together = (('feature', 'slug'),)

