import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dev")
DEBUG = os.getenv("DEBUG", "0") == "1"
ALLOWED_HOSTS = [h.strip() for h in os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")]


INSTALLED_APPS = [
"django.contrib.admin","django.contrib.auth","django.contrib.contenttypes",
"django.contrib.sessions","django.contrib.messages","django.contrib.staticfiles",
"django.contrib.gis",
"rest_framework","corsheaders","core",
]
MIDDLEWARE = [
"corsheaders.middleware.CorsMiddleware",
"django.middleware.security.SecurityMiddleware",
"whitenoise.middleware.WhiteNoiseMiddleware",
"django.contrib.sessions.middleware.SessionMiddleware",
"django.middleware.common.CommonMiddleware",
"django.middleware.csrf.CsrfViewMiddleware",
"django.contrib.auth.middleware.AuthenticationMiddleware",
"django.contrib.messages.middleware.MessageMiddleware",
]
ROOT_URLCONF = "app.urls"
TEMPLATES = [{
"BACKEND":"django.template.backends.django.DjangoTemplates",
"DIRS":[BASE_DIR/"templates"],
"APP_DIRS":True,
"OPTIONS":{"context_processors":[
"django.template.context_processors.debug",
"django.template.context_processors.request",
"django.contrib.auth.context_processors.auth",
"django.contrib.messages.context_processors.messages",
]},
}]
WSGI_APPLICATION = "app.wsgi.application"


DATABASES = {"default":{
"ENGINE":"django.contrib.gis.db.backends.postgis",
"NAME":os.getenv("DB_NAME","lbs"),
"USER":os.getenv("DB_USER","lbs"),
"PASSWORD":os.getenv("DB_PASSWORD","lbs"),
"HOST":os.getenv("DB_HOST","127.0.0.1"),
"PORT":os.getenv("DB_PORT","5432"),
}}


AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/Dublin"
USE_I18N = True
USE_TZ = True
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR/"staticfiles"
CORS_ALLOW_ALL_ORIGINS = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
"DEFAULT_RENDERER_CLASSES":["rest_framework.renderers.JSONRenderer"],
"DEFAULT_PARSER_CLASSES":["rest_framework.parsers.JSONParser"],
}