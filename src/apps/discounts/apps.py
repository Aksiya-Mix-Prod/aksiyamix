from django.apps import AppConfig


class DiscountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.discounts'


    def ready(self):
        import apps.discounts.signals