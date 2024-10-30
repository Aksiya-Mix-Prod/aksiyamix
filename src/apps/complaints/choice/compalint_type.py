from django.db import models


class ComplaintType(models.IntegerChoices):
    NAME_OF_COMPANY = 0, 'Username of Company'
    DISCOUNT = 1, 'Discount'
    COMPANY = 2, 'Company'
    DONT_LIKE = 3, 'Don`t like'
    VIOLENCE = 4, 'Violence'
    ILLEGAL_PRODUCTS = 5, 'Illegal Products'
    PORNOGRAPHIC_MATERIALS = 6, 'Pornographic_materials'
    TERRORISM = 7, 'Terrorism'
    FRAUD = 8, 'Fraud'
    PERSONAL_DATA = 9, 'Personal data'
    OTHERS = 10, 'Others'