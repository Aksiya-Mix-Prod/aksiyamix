from django.conf import settings

LANGUAGE_CODE = 'ru'

LANGUAGES = [
    ('uz', 'Uzbek'),
    ('ru', 'Russian'),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_LANGUAGE = ('ru', 'uz')

USE_I18N = True

LOCALE_PATHS = [
    settings.BASE_DIR / 'locale',
]