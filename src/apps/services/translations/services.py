from modeltranslation.translator import TranslationOptions, register

from apps.services.models import Service


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name',)