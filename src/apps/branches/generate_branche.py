from faker import Faker
from random import choice, randint
from apps.companies.models.company import Company  # Import your BranchCompany and Company models
from apps.branches.models.branch import BranchCompany
from apps.base.utils.region_choices import Regions, District  # Import necessary choices

fake = Faker()

def generate_branch_company():
    # Get a random active, verified company
    company = Company.objects.filter(is_active=True, is_verified=True, is_deleted=False).first()

    if company is None:
        print("No active, verified company found.")
        return None

    # Generate fake branch company data
    title = fake.company()
    phone_number1 = fake.phone_number()
    phone_number2 = fake.phone_number()
    address = fake.address()

    # Get random region and district
    region = choice([region[0] for region in Regions.choices])  # Choose a valid region
    district = choice([district[0] for district in District.choices])  # Choose a valid district

    # Random delivery option
    delivery = choice([True, False])

    # Random geographic coordinates
    latitude = fake.latitude()
    longitude = fake.longitude()

    # Generate a unique id for the branch
    id_branch = randint(1000, 9999)  # Example: generate random 4-digit number

    # Create the branch company instance
    branch_company = BranchCompany.objects.create(
        company=company,
        id_branch=id_branch,
        title=title,
        phone_number1=phone_number1,
        phone_number2=phone_number2,
        address=address,
        region=region,
        district=district,
        delivery=delivery,
        longitude=longitude,
        latitude=latitude
    )

    return branch_company


# Example usage
generate_branch_company()
