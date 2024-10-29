from django.contrib import admin

from .models.company import Company
from .models.company_time_table import CompanyTimeTable


admin.site.register(Company)
admin.site.register(CompanyTimeTable)