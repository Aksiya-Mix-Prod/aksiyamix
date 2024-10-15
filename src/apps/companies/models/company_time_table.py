from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from src.apps.companies.models.company import Company
from src.apps.companies.enums.week_day import WeekDay
from src.apps.base.models.base import AbstractBaseModel
from src.apps.companies.models.branch import BranchCompany


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

    week_day = models.PositiveSmallIntegerField(choices=WeekDay.choices)

    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = (('company', 'week_day'),
                           ('branch_company', 'week_day'))

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError(_('start_time must be lower than end_time!'))