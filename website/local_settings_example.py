"""
local settings, included in settings.py
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: Make this unique, and don't share it with anybody.
SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(BASE_DIR, 'dev.sqlite'),                      # Or path to database file if using sqlite3.
    }
}

LANGUAGE_CODE = 'en-US'

TIME_ZONE = "Europe/Amsterdam"

#STATIC_ROOT = '/home/username/webapps/<staticdir>/'
STATIC_ROOT = ''

#STATIC_URL = '//www.domain.com/static/'
STATIC_URL = '/static/'

#MEDIA_ROOT = '/home/<username>/webapps/<projectstatic>/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'website/static/media/')

#MEDIA_URL = '//www.<your-domain>.com/static/media/'
MEDIA_URL = '/static/media/'


# Login and Registration
REGISTRATION_OPEN = True


# Contact details
CONTACT_EMAIL = 'info@example.com'
