from django.core.validators import MinValueValidator
from django.db import models

from apps.base.models import AbstractBaseModel


class CompanyTopTariff(AbstractBaseModel):
    company = models.ForeignKey(to='companies.Company', 
                                on_delete=models.PROTECT, 
                                related_name='top_tariffs', 
                                null=True,
                                limit_choices_to={
                                    'is_deleted': False,
                                    'is_active': True
                                })

    quantity = models.PositiveIntegerField(default=0, editable=False)
    price = models.DecimalField(max_digits=10, 
                                decimal_places=2, 
                                default=0, 
                                validators=[MinValueValidator(0)], 
                                editable=False)

    class Meta:
        db_table = 'company_top_tariff'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        company_tops = self.company.top_tariff_counts
        self.company.top_tariff_counts = str(int(company_tops) + self.quantity)
        self.company.save()

    def __str__(self):
        return f"{self.quantity}-{self.price}"