import os.path
from pathlib import Path

from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+c@gn$y8hptse+k*-5ca56qe2134mcwymb9fkws1i48+kyv1p=89(a-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'news.apps.NewsConfig',
    'django_filters',
    'sign',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',

    # apscheduler
    'django_apscheduler',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # allauth
    'allauth.account.middleware.AccountMiddleware',

    # Кэширование всего сайта
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Добавление адреса перенаправления после успешного входа в систему в файл настроек проекта (settings.py):
LOGIN_URL = '/accounts/login/'
SITE_ID = 1
LOGIN_REDIRECT_URL = reverse_lazy("mails:news_list")

# email
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'imaralievasadbek'  # ваше имя пользователя, например, если ваша почта user@yandex.ru, то сюда надо писать user, иными словами, это всё то что идёт до собаки
EMAIL_HOST_PASSWORD = 'apvuvdxxueyomifk'  # пароль от почты(а не от аккаунта)
EMAIL_USE_SSL = True  # Яндекс использует ssl, подробнее о том, что это, почитайте в дополнительных источниках, но включать его здесь обязательно
# mail-admins
# ADMINS = [
#     ('asad', 'imaraliev.kg2005@gmail.com'),
#     ('bek', 'asadullahgits@gmail.com'),
# ]
# SERVER_EMAIL = 'imaralievasadbek@yandex.ru'
# mail-menagers
MANAGERS = [
    ('asad', 'imaraliev.kg2005@gmail.com'),
    ('bek', 'imaraliev.kg2005@gmail.com'),
]
SERVER_EMAIL = 'imaralievasadbek@yandex.ru'

#  Регистрация по электронной почте.
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'


'''
    Чтобы allauth распознал нашу форму как ту, 
    что должна выполняться вместо формы по умолчанию, 
    необходимо добавить строчку в файл настроек проекта settings.py:
'''
ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}



# celery
CELERY_BROKER_URL = 'redis://:vqvFPAmVeX3zClKHhxB4dKIXQoLX3Brm@redis-16650.c259.us-central1-2.gce.cloud.redislabs.com:16650'
CELERY_RESULT_BACKEND = 'redis://:vqvFPAmVeX3zClKHhxB4dKIXQoLX3Brm@redis-16650.c259.us-central1-2.gce.cloud.redislabs.com:16650'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


DEFAULT_FROM_EMAIL = EMAIL_HOST_USER + '@yandex.ru'  # здесь указываем уже свою ПОЛНУЮ почту, с которой будут отправляться письма

# apscheduler
# формат даты, которую будет воспринимать наш задачник (вспоминаем модуль по фильтрам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# если задача не выполняется за 25 секунд, то она автоматически снимается, можете поставить время побольше, но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds




# # # caches
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
#         'TIMEOUT': 30,
#         # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
#     }
#
# }

