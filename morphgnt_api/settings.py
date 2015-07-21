import os

import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g7j+tn)pjz_sw7j3$z_c*^6gwv43b7!%1&#!nt2)q2u&6i#@qx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "morphgnt_api",
]
MIDDLEWARE_CLASSES = []

ROOT_URLCONF = "morphgnt_api.urls"
WSGI_APPLICATION = "morphgnt_api.wsgi.application"


# Database

DATABASES = {
    "default": dj_database_url.config(default="postgres://localhost/morphgnt_api")
}
