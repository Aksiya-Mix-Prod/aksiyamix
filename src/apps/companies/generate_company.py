from faker import Faker
from random import randint, choice
from django.core.files.base import ContentFile
import os
from io import BytesIO
from django.core.files.storage import default_storage
from apps.companies.models.company import Company  # Make sure to import your model
from apps.categories.models.category import Category  # For the ManyToManyField relation

fake = Faker()


def generate_company():
    # Generate fake owner details
    owner_first_name = fake.first_name()
    owner_last_name = fake.last_name()
    owner_father_name = fake.first_name()
    owner_phone_number1 = fake.phone_number()
    owner_phone_number2 = fake.phone_number()

    # Generate company fields
    name = fake.company()
    username = fake.slug()
    email = fake.email()
    address = fake.address()
    phone_number = fake.phone_number()
    is_verified = choice([True, False])
    is_active = choice([True, False])
    is_deleted = False
    is_spammed = False

    # Create random geographic information
    regions = [1, 2, 3]  # Example region ids
    districts = ["District1", "District2", "District3"]
    region = choice(regions)
    district = choice(districts)

    # Create company counts (you can simulate random data for these)
    follower_counts = randint(0, 1000)
    like_counts = randint(0, 1000)
    dislike_counts = randint(0, 1000)
    comment_counts = randint(0, 1000)
    view_counts = randint(0, 1000)

    # Use an image URL generator for the logo and banner (mock image creation)
    logo_url = fake.image_url()
    banner_url = fake.image_url()
    logo = generate_image(logo_url)
    banner = generate_image(banner_url)

    # Generate random coordinates for latitude and longitude
    latitude = fake.latitude()
    longitude = fake.longitude()

    # Generate random description and website
    short_description = fake.sentence()
    long_description = fake.paragraph()
    web_site_url = fake.url()

    # Set balance and ratings
    balance = randint(0, 10000)
    total_ratings = randint(0, 5)
    rating5 = randint(0, 100)
    rating4 = randint(0, 100)
    rating3 = randint(0, 100)
    rating2 = randint(0, 100)
    rating1 = randint(0, 100)

    # Get random categories (ManyToManyField)
    categories = Category.objects.all()
    selected_categories = [choice(categories) for _ in range(3)]

    # Create company instance
    company = Company.objects.create(
        owner_first_name=owner_first_name,
        owner_last_name=owner_last_name,
        owner_father_name=owner_father_name,
        owner_phone_number1=owner_phone_number1,
        owner_phone_number2=owner_phone_number2,
        name=name,
        username=username,
        email=email,
        address=address,
        phone_number=phone_number,
        is_verified=is_verified,
        is_active=is_active,
        is_deleted=is_deleted,
        is_spammed=is_spammed,
        regions=region,
        districts=district,
        follower_counts=follower_counts,
        like_counts=like_counts,
        dislike_counts=dislike_counts,
        comment_counts=comment_counts,
        view_counts=view_counts,
        logo=logo,
        banner=banner,
        latitude=latitude,
        longitude=longitude,
        short_description=short_description,
        long_description=long_description,
        web_site_url=web_site_url,
        balance=balance,
        total_ratings=total_ratings,
        rating5=rating5,
        rating4=rating4,
        rating3=rating3,
        rating2=rating2,
        rating1=rating1
    )

    # Add the categories to the company
    company.categories.set(selected_categories)

    return company


# Function to generate an image (mocked)
def generate_image(url):
    image = fake.image()
    file_name = url.split("/")[-1]
    file_path = os.path.join("companies/logos", file_name)

    # Create a file object
    file_obj = ContentFile(image.encode())
    image_file = BytesIO(file_obj.read())
    storage_path = default_storage.save(file_path, image_file)
    return storage_path


# Example usage
generate_company()
