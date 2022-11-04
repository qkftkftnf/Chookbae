"""
Django settings for chookbae project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from secret import db_setting
# import environ
import secret.email_setting as email_setting
import secret.apikey as apikey
# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )

# reading .env file
# environ.Env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9xx1qky5j(sc!m!-#8#befht@z68j8*=-0jiv#gheq(!fhy39+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['k7a202.p.ssafy.io']
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'worldcup',
    'accounts',
    'rest_framework',
    # 'rest_framework_simplejwt',
    # 'django.contrib.sites',
    # 'allauth.account',
    # 'allauth.socialaccount',
    'storages',
    'six',
    'imagekit',
    'django_apscheduler',
    'drf_yasg',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
SITE_ID = 1
AUTH_USER_MODEL = 'accounts.User'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 가능한 한 위에 배치
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',  # 인증된 요청인지 확인
#         'rest_framework.permissions.IsAdminUser',  # 관리자만 접근 가능
#         'rest_framework.permissions.AllowAny',  # 누구나 접근 가능
#     ),
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT를 통한 인증방식 사용
#     ),
# }
REST_USE_JWT = True


from datetime import timedelta
SIMPLE_JWT = {
    'SIGNING_KEY': SECRET_KEY,
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
}

#CORS 허용
CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'chookbae.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR],
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

WSGI_APPLICATION = 'chookbae.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = db_setting.DATABASES



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = {
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
}

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_USER = email_setting.EMAIL_HOST_USER
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_HOST_PASSWORD = email_setting.EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_MAIL = EMAIL_HOST_USER
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_AUTHENTICATION_METHOD = 'email' #로그인 시 이메일로 로그인
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 0.02 # 30분 경과시 비활성화
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[Chookbae]이메일 인증' # 이메일 제목 앞에 붙는 prefix



AWS_ACCESS_KEY_ID = apikey.AWS_ACCESS_KEY_ID # .csv 파일에 있는 내용을 입력 Access key ID
AWS_SECRET_ACCESS_KEY = apikey.AWS_SECRET_ACCESS_KEY # .csv 파일에 있는 내용을 입력 Secret access key
AWS_REGION = apikey.AWS_REGION # 리전
AWS_STORAGE_BUCKET_NAME = apikey.AWS_STORAGE_BUCKET_NAME # 설정한 이름
AWS_S3_CUSTOM_DOMAIN = apikey.AWS_S3_CUSTOM_DOMAIN
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'chookbae.asset_storage.MediaStorage' # 파일 저장소를 S3로 설정
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'chookbae.asset_storage.MediaStorage'
STATICFILES_DIRS = [
    BASE_DIR/'static'
]
