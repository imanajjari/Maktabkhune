from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-to+@s&==_c_zf4%p3c(ztc*^n-*vsdj@dpff%*!ue+ibt@tl_r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#sites framework
SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS =[
    BASE_DIR / 'static/',
]

MEDIA_ROOT = BASE_DIR / 'media'

X_FRAME_OPTIONS = 'SAMEORIGIN'
