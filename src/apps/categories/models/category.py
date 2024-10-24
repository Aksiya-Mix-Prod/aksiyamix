from django.db import models
from django.utils.text import slugify

from apps.base.models import AbstractBaseModel
from apps.base.exceptions import CustomExceptionError
from apps.categories.validators.image_size import parent_category_image_size

class Category(AbstractBaseModel):
    """
    Category Model
    """

    name = models.CharField(max_length=255, name="name")
    slug = models.SlugField(max_length=255)

    parent = models.ForeignKey(
        to='self',
        on_delete=models.PROTECT,
        related_name='children',
        blank=True,
        null=True,
        help_text='parent category of child categories'
    )

    icon = models.ImageField(upload_to='categories/icons/%Y/%m/%d', blank=True, null=True)


    def clean(self):
        self.slug = slugify(self.name)
        if Category.objects.filter(parent_id=self.parent.pk, slug=self.slug).exists():
            raise CustomExceptionError(code=400, detail={'name': 'this category has already exists'})
    
    class Meta:
        db_table = "category"
        verbose_name_plural = "Categories"
        unique_together = (('parent', 'slug'),)

    def clean(self):
        """
        Category Validation
        """

        # ========== CHECK CATEGORY 3 LEVEL =======

        try:
            if not self.pk and self.parent.parent.parent:
                raise CustomExceptionError(code=400, detail={'parent': 'Category must be 3 level degree'})
        except AttributeError:
            pass

        # ========== CHECK IF 1 DEGREE CATEGORY HAVE AN ICON ==========

        if not self.parent and not self.icon:
            raise CustomExceptionError(code=400, detail={'icon': '1-level degree category must have an icon !'})

    def __str__(self):
        return self.name