import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '_1gc)s64_ms)9^r*191q!6_#=2%s5aczb47wo7sc%6oi@u7zm2'

DEBUG = False

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
# CORS_ORIGIN_WHITELIST = [
#     "http://127.0.0.1:8266",
#     "http://localhost:8266"
# ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'api',
    'main.apps.AppGlobalConfig'
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'main.filter_middleware.PermissionMiddleware',
# ]

ROOT_URLCONF = 'main.urls'

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

WSGI_APPLICATION = 'main.wsgi.application'

# config permission url

EVERCALL_API_URL_ACCESS = ['/', '/rest/api/authen/login']
EVERCALL_API_PERMISSION_ACCESS = ['/rest/api/authen/logout']

# Database Mysql

MSQL_MOBILE_DEMO_INFO_HOST = '192.168.66.69'
MSQL_MOBILE_DEMO_INFO_POST = 3306
MSQL_MOBILE_DEMO_INFO_DB = 'mydb'
MSQL_MOBILE_DEMO_INFO_USER = 'admin'
MSQL_MOBILE_DEMO_INFO_PASS = 'Evercall@123'

# Validation

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
