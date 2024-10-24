import random
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from apps.companies.models.company import Company
from apps.companies.enums.week_day import WeekDay
from apps.base.models.base import AbstractBaseModel
from apps.companies.models.branch import BranchCompany


class CompanyTimeTable(AbstractBaseModel):
    """
    Here creating company timetable
    """
    company = models.ForeignKey(Company, on_delete=models.PROTECT,
                                blank=True, null=True,
                                limit_choices_to={
                                    'is_active': True,
                                    'is_verified': True,
                                    'is_deleted': False
                                }
    )
    branch_company = models.ForeignKey(BranchCompany,
                                       on_delete=models.PROTECT,
                                       blank=True,
                                       null=True,
                                       limit_choices_to={
                                           'is_active': True,
                                           'is_deleted': False
                                       })

    id_company_time_table = models.PositiveSmallIntegerField(unique=True, editable=False)

    week_day = models.PositiveSmallIntegerField(choices=WeekDay.choices)

    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = (('company', 'week_day'),
                           ('branch_company', 'week_day'))

    def save(self, *args, **kwargs):
        """
        Generate a unique advertisement ID for new instances before saving
        """
        if self.pk is None:
            self.id_company_time_table = self.generate_company_time_table_id()
        super().save(*args, **kwargs)

    def generate_company_time_table_id(self):
        """
        Generate a unique 8-digit advertisement ID.
        """
        while True:
            # Generate an 8-digit number

            new_id = random.randint(10000000, 99999999)
            # Check for uniqueness
            if not CompanyTimeTable.objects.filter(id_company_time_table=new_id).exists():
                return new_id

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError(_('start_time must be lower than end_time!'))