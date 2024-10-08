from pathlib import Path
import os
from os import getenv
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

#SECRET_KEY = config("SECRET_KEY") windows env setting

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
# development
# DEBUG = True
# ALLOWED_HOSTS = []

# production
DEBUG = False
ALLOWED_HOSTS = ["api.grabbofertilityclinic.com", "www.api.grabbofertilityclinic.com"]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    "clinic",
    'corsheaders',
    "anymail",
    'drf_yasg',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'grabbo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'grabbo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'grabbo',
#         'USER': 'postgres',
#         'PASSWORD': 'austinforreal',
#         'PORT': '5433',
#         'HOST': 'localhost'

#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': getenv('DB_NAME'),
        'USER': getenv('DB_USER'),
        'PASSWORD': getenv('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

##developments
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [

#     # os.path.join(BASE_DIR, 'static')

# ]
# STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



#production
STATIC_URL = '/static/'

STATICFILES_DIRS = [
  BASE_DIR/ 'assets'
]

STATIC_ROOT = BASE_DIR/ 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/ 'media'




REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}



CORS_ALLOW_ALL_ORIGINS= False
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3002",
    "https://grabbofertilityclinic.com",
    "https://www.grabbofertilityclinic.com",
    "https://api.grabbofertilityclinic.com",
    "https://www.api.grabbofertilityclinic.com",
]


CORS_ORIGIN_WHITELIST = [
    "http://localhost:3002",
   "https://grabbofertilityclinic.com",
     "https://www.grabbofertilityclinic.com",
        "https://api.grabbofertilityclinic.com",
     "https://www.api.grabbofertilityclinic.com",
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = "anymail.backends.resend.EmailBackend"
ANYMAIL = {

    "RESEND_API_KEY": os.getenv('RESEND_API_KEY') ,
}

EMAIL_SUBJECT_PREFIX="Grabbo Fertility Clinic"
DEFAULT_FROM_EMAIL = 'contact@grabbofertilityclinic.com'
SERVER_EMAIL = 'contact@grabbofertilityclinic.com'
