from apps.services.models import Service


services_name = [
    'delivery',
    'installation',
    'repair',
    'consultation',
    'maintenance',
    'training',
    'tune',
    'exchange',
    'service',
    'other',    
    ]

def generate_services(services_name):
    services = []
    for service_name in services_name:
        service = Service(name=service_name, is_active=True)
        services.append(service)
    Service.objects.bulk_create(services)