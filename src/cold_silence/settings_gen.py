from cold_silence.utils import (
    write_to_file,
    DEFAULT_PATH,
    DEFAULT_PROJECT_NAME,
    ENGINE_SQLITE3,
)
import os


class SettingsGen:
    def __generate_database_config(self, engine):
        db_config = (
            """
"USER": get_env_value("DB_USER"),
"PASSWORD": get_env_value("DB_PASS"),
"HOST": get_env_value("DB_HOST"),
"PORT": get_env_value("DB_PORT"),
"""
            if engine is not ENGINE_SQLITE3
            else ""
        )

        return """
DATABASES = {{
    "default": {{
        "ENGINE": "django.db.backends.{0}",
        "NAME": get_env_value("DB_TABLE"),
        {1}
    }}
}}
    """.format(
            engine, db_config
        )

    def __generate_settings_file_content(
        self, project_name=DEFAULT_PROJECT_NAME, engine=ENGINE_SQLITE3
    ):
        try:
            import django

            django_version = django.VERSION

            django_major_version = "{0}.{1}".format(
                django_version[0], django_version[1]
            )

            db_config = self.__generate_database_config(engine=engine)

            content = """
\"\"\"
Django settings for {0} project.

Generated by 'django-admin startproject' using Django {1}.

For more information on this file, see
https://docs.djangoproject.com/en/{2}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{2}/ref/settings/
\"\"\"

from django.core.exceptions import ImproperlyConfigured
from pathlib import Path
import os


def get_env_value(env_variable):
    try:
      	return os.environ[env_variable]
    except KeyError:
        error_msg = "Set the {{0}} environment variable".format(env_variable)
        raise ImproperlyConfigured(error_msg)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_value("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env_value("DEBUG")

ALLOWED_HOSTS = [i for i in get_env_value("ALLOWED_HOSTS").split(",")]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "{0}.urls"

TEMPLATES = [
    {{
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {{
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        }},
    }},
]

WSGI_APPLICATION = "{0}.wsgi.application"

# Database

{3}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {{
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    }},
    {{"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",}},
    {{"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",}},
    {{"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",}},
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"
        """.format(
                project_name, django.__version__, django_major_version, db_config
            )

        except Exception as e:
            raise e

        return content

    def generate_settings_file(
        self,
        path=DEFAULT_PATH,
        project_name=DEFAULT_PROJECT_NAME,
        engine=ENGINE_SQLITE3,
    ):
        settings_file_path = "{0}/settings.py".format(path)

        content = self.__generate_settings_file_content(
            project_name=project_name, engine=engine
        )

        write_to_file(settings_file_path, contents=content)
