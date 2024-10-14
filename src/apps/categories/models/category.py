from django.db import models

from src.apps.base.models import AbstractBaseModel
from src.apps.base.exceptions import CustomExceptionError


class Category(AbstractBaseModel):
    """
    Model for category to use in company model, discount model and etc.
    """

    # name information
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25, unique=True)

    # parent category of child categories
    parent = models.ForeignKey(
        to='self',
        on_delete=models.PROTECT,
        related_name='children',
        blank=True, null=True
    )

    # icon information
    icon = models.ImageField(upload_to='categories/icons/%Y/%m/%d', blank=True, null=True)

    
    class Meta:
        db_table = "category"
        verbose_name_plural = "Categories"

    def clean(self):
        """
        to validate data before saving it.
        """

        # ========== CHECK CATEGORY 3 LEVEL =======

        try:
            if not self.pk and self.parent.parent.parent:
                raise CustomExceptionError(400, {'parent': 'Category must be 3 level degree'})
        except AttributeError:
            pass

        # ========== CHECK IF 1 DEGREE CATEGORY HAVE AN ICON ==========

        if not self.parent and not self.icon:
            raise CustomExceptionError(400, '1-level degree category must have an icon !')

    def __str__(self):
        return self.name