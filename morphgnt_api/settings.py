import os

import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g7j+tn)pjz_sw7j3$z_c*^6gwv43b7!%1&#!nt2)q2u&6i#@qx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get("DEBUG", "1")))

ALLOWED_HOSTS = [
    "localhost",
    "api.morphgnt.org",
    "*.herokuapp.com"
]


# Application definition

INSTALLED_APPS = [
    "morphgnt_api",
    "corsheaders",
]
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "morphgnt_api.urls"
WSGI_APPLICATION = "morphgnt_api.wsgi.application"


# Database

DATABASES = {
    "default": dj_database_url.config(default="postgres://localhost/morphgnt_api")
}

CORS_ORIGIN_ALLOW_ALL = True
