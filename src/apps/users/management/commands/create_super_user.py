from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand): 
    def handle(self, *args, **options):
        email = None
        phone_number = "+998999999999"
        password = "1"
        full_name = "Super User"
        super_user = get_user_model().objects.create_superuser(email=email, phone_number=phone_number, password=password, fullname=full_name)
        
        self.stdout.write(self.style.SUCCESS(
            f'{super_user} users created\nemail= {email}\nphone_number= {phone_number}\npassword= {password}'))
