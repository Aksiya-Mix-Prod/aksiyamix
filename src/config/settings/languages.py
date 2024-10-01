from django.conf import settings


LANGUAGE_CODE = 'uz'

LANGUAGES = [
    ('uz', 'Uzbek'),
    ('ru', 'Russian'),
]

MODELTRNSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRNSLATION_LANGUAGE = ('ru', 'uz')

USE_I18N = True

LOCALE_PATHS = [
    settings.BASE_DIR / 'locale',
]