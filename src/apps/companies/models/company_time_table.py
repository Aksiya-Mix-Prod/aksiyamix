from django.core.exceptions import ValidationError
from django.db import models

from src.apps.companies.models.company import Company
from src.apps.companies.models.branch import BranchCompany
from src.apps.companies.enums.week_day import WeekDay
from src.apps.base.models.base import AbstractBaseModel


class CompanyTimeTable(AbstractBaseModel):
    """
    Here creating company timetable
    """
    company = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True, null=True)
    branch_company = models.ForeignKey(BranchCompany, on_delete=models.PROTECT, blank=True, null=True)

    week_day = models.PositiveSmallIntegerField(choices=WeekDay.choices)

    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = (('company', 'week_day'),
                           ('branch_company', 'week_day'))

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError('start_time must be lower than end_time!')