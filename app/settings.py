import os
from pathlib import Path

import mimetypes
mimetypes.add_type("text/css", ".css", True)


if os.environ.get('ENVIRONMENT', 'dev') == 'dev':
    from dotenv import load_dotenv
    load_dotenv()

# SETTING UP ENVIRONMET VARIABLES FOR EASY ACCESS THROUGHOUT THE APPLICATION
env = {
    'ENVIRONMENT': os.environ.get('ENVIRONMENT', 'dev'),  # Check for production environment
    'SECRET_KEY': os.environ.get('SECRET_KEY', '_yw0ks9qv&0(jtvd$6_oguc80h'),
    'DEBUG': bool(os.environ.get('DEBUG')),
    'HOSTS': os.environ.get('HOSTS', None),
    'DB': {
        'EXTERNAL_DB': bool(os.environ.get('DB')),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD')
    }
}

# Build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env['DEBUG']

ALLOWED_HOSTS = ['localhost']

# add more hosts without changing the source code
external_hosts = env['HOSTS']
if external_hosts is not None:
    ALLOWED_HOSTS.extend(external_hosts.split('/'))


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'core',
    'user',
    'recipe'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if env['DB']['EXTERNAL_DB']:
    # external database (postgres) defined in environment
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': env['DB']['HOST'],
            'PORT': env['DB']['PORT'],
            'NAME': env['DB']['NAME'],
            'USER': env['DB']['USER'],
            'PASSWORD': env['DB']['PASSWORD']
        }
    }
else:
    # use sqlite db
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Extra places for collectstatic to find static files.
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "media"),)

# Setup Custom UserModel
AUTH_USER_MODEL = 'core.User'

# print all environment variables good for debugging funky behaviour in production
if bool(os.environ.get('PRINT_ENVIRONMENT_VARIABLES', False)):
    import pprint
    pp = pprint.PrettyPrinter(depth=4)
    pp.pprint(env)

print("DEBUG:", DEBUG)
