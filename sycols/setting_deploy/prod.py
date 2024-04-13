from sycols.settings import *


SECRET_KEY = 'django-insecure-*pe&p!k&%40sw+f81&ku2rbyr!^tr(mof#t*9f!t0qn6fsl&fe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mohsen-piri.com', 'www.mohsen-piri.com']

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

STATIC_ROOT = '/home/mohsenpi/public_html/static'
MEDIA_ROOT = '/home/mohsenpi/public_html/media'



# HSTS setting
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
# Https setting
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
# more security setting
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

SECURE_REFERRER_POLICY = 'strict-origin'
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SAMESITE = 'Strict'
CSRF_COOKIE_HTTPONLY = True
CSRF_USE_SESSIONS = True
