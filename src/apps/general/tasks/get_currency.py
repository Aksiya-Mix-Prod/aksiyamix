import requests

from celery import shared_task

# from apps.general.models.general import Currency

@shared_task
def get_currency():
    url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'

    response = requests.get(url=url)

    one_usd_in_uzs = response.json()[0]['Rate']

    established_date = response.json()[0]['Date']

    print(one_usd_in_uzs, established_date)

