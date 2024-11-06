import random
from django.db import models
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _

from apps.companies.enums.week_day import WeekDay
from apps.base.models.base import AbstractBaseModel
from apps.base.exceptions import CustomExceptionError


class CompanyTimeTable(AbstractBaseModel):
    """
    Here creating company timetable
    """
    company = models.ForeignKey('companies.Company', on_delete=models.PROTECT,
                                blank=True, null=True,
                                limit_choices_to={
                                    # 'is_active': True,
                                    'is_verified': True,
                                    'is_deleted': False
                                }
    )
    branch_company = models.ForeignKey('branches.BranchCompany',
                                       on_delete=models.PROTECT,
                                       blank=True,
                                       null=True,
                                       limit_choices_to={
                                           # 'is_active': True,
                                           # 'is_deleted': False
                                       })

    id_company_time_table = models.PositiveSmallIntegerField(unique=True, editable=False)

    week_day = models.PositiveSmallIntegerField(choices=WeekDay.choices)

    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        constraints = [
            UniqueConstraint(fields=['company', 'week_day'], name='unique_company_week_day'),
            UniqueConstraint(fields=['branch_company', 'week_day'], name='unique_branch_company_week_day'),
        ]

    def clean(self):
        """
        Generate a unique CompanyTimeTable ID for new instances before saving
        """
        if self.pk is None:
            self.id_company_time_table = self.generate_company_time_table_id()

        if self.start_time > self.end_time:
            raise CustomExceptionError(_(code=400, detail='start_time must be lower than end_time!'))

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

