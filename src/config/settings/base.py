import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# (?<data>img/[a-zA-Z0-9/._-]+)
# {% static '${data}' %}

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ['SECRET_KEY']

REDIS_PORT_URL = os.environ['REDIS_PORT_URL']

DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True

INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',  
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'debug_toolbar',
    'django_ckeditor_5',
    'django_celery_beat',
    'django_celery_results',
    'corsheaders',
    'drf_yasg',
]

INSTALLED_APPS += [
    'apps.advertisements.apps.AdvertisementsConfig',
    'apps.appeals.apps.AppealsConfig',
    'apps.authentication.apps.AuthenticationConfig',
    'apps.base.apps.BaseConfig',
    'apps.boosts.apps.BoostsConfig',
    'apps.branches.apps.BranchesConfig',
    'apps.categories.apps.CategoriesConfig',
    'apps.comments.apps.CommentsConfig',
    'apps.companies.apps.CompaniesConfig',
    'apps.complaints.apps.ComplaintsConfig',
    'apps.discounts.apps.DiscountsConfig',
    'apps.features.apps.FeaturesConfig',
    'apps.followers.apps.FollowersConfig',
    'apps.general.apps.GeneralConfig',
    'apps.likes.apps.LikesConfig',
    'apps.notifications.apps.NotificationsConfig',
    'apps.packets.apps.PacketsConfig',
    'apps.payments.apps.PaymentsConfig',
    'apps.products.apps.ProductsConfig',
    'apps.ratings.apps.RatingsConfig',
    'apps.services.apps.ServicesConfig',
    'apps.tags.apps.TagsConfig',
    'apps.tops.apps.TopsConfig',
    'apps.users.apps.UsersConfig',
    'apps.wishlists.apps.WishlistsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',  
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


TIME_ZONE = 'Asia/Tashkent'

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR / 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'