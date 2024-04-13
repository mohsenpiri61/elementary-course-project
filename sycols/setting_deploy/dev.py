from sycols.settings import *

SECRET_KEY = 'django-insecure-*pe&p!k&%40sw+f81&ku2rbyr!^tr(mof#t*9f!t0qn6fsl&fe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

SITE_ID = 2


# summernote setting
SUMMERNOTE_THEME = 'bs4'
if DEBUG:
    X_FRAME_OPTIONS = "SAMEORIGIN"
else:
    X_FRAME_OPTIONS = 'DENY'
SUMMERNOTE_CONFIG = {
    'iframe': True,
    'summernote': {
        'airMode': False,
        # Use proper language setting automatically (default)
        'lang': None,
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],
    },
}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_project',
        'USER': 'mohsen',
        'PASSWORD': 'a123@123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [BASE_DIR / "assets", ]
