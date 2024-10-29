import random
from datetime import timedelta
from django.utils import timezone
from apps.advertisements.models import Advertisement


def generate_advertisements():
    """
    Generate 10 Advertisement objects with unique titles and random sample data.
    """
    # Base values for dates
    start_date = timezone.now().date()
    end_date = start_date + timedelta(days=30)

    advertisements = []

    for i in range(1, 11):
        advertisement = Advertisement(
            id_advertisement=generate_unique_ad_id(),
            title=f'Unique Advertisement {i}',  # Ensure unique title
            image=f'advertisements/images/sample_image_{i}.jpg',  # Sample image path
            url_link=f'https://example.com/advertisement/{i}',
            ordering=random.randint(1, 100),
            start_date=start_date,
            end_date=end_date,
        )
        advertisements.append(advertisement)

    # Use bulk_create to save all objects at once
    Advertisement.objects.bulk_create(advertisements)
    print("10 Advertisement objects created successfully.")


def generate_unique_ad_id():
    """
    Generate a unique 8-digit ID for advertisement.
    """
    while True:
        new_id = random.randint
