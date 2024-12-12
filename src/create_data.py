import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'


django.setup()

from django.utils.timezone import now, timedelta
from apps.categories.models import Category
from apps.companies.models import Company
from apps.users.models import CustomUser
from apps.discounts.models import Discount

owner = CustomUser.objects.first()


cat1 = Category.objects.create(name='Category 1', slug='category-1', icon="asdy")
print('cat1 create')
cat2 = Category.objects.create(name='Category 2', slug='category-2', parent=cat1)
print('cat2 create')
cat3 = Category.objects.create(name='Category 3', slug='category-3', parent=cat2)
print('cat3 create')


company = Company.objects.create(
    owner=owner, 
    owner_last_name="Mufassaev",
    owner_first_name="Simba",
    owner_father_name="Sherivich",
    owner_phone_number1="+998994337104",
    owner_phone_number2="+998994437104",
    regions=1,
    is_active=True,
    districts="1X1",
    name="Korzinka",
    username="korz",
    address="qattadur",
    phone_number="+998999999999",
    short_description="vashe zo'r magazin",
    long_description="lekin sal bo'maganro",
    longitude=9009809809809,
    latitude=9009897988768,)
print(f'company create {company.id}')


for i in range(30):
    Discount.objects.create(
        company=company,
        first_category_id=cat1.id, 
        second_category_id=cat2.id, 
        category_id=cat3.id, 
        status=3, 
        discount_type=1, 
        currency=2, 
        is_active=True, 
        title=f"tell {i}", 
        price=1000, 
        old_price=1500, 
        description="vashe zo'r tell", 
        image="asdasd", 
        quantity=120, 
        remainder=90, 
        start_date=now().date(),
        end_date=now().date() + timedelta(days=30), 
        discount_value=30, 
        discount_value_is_percent=True,)
    print(f'discount {i} create')