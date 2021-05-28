from string import ascii_letters, digits, punctuation
import errno
import os
import random
import pip

DEFAULT_PATH = "project_output"

DEFAULT_SERVICE_NAME = "django"

DEFAULT_PROJECT_NAME = "project"

DEFAULT_PROJECT_DIRECTORY = "project"

DEFAULT_SERVER_PORT = 8000

DEFAULT_DEBUG = True

DEFAULT_CONFIG = {}

ENGINE_SQLITE3 = "sqlite3"

ENGINE_POSTGRESQL = "postgresql"

ENGINE_MYSQL = "mysql"

ENGINE_ORACLE = "oracle"

# Environments
LOCAL = "local"
DEV = "dev"
STAGING = "staging"
PROD = "prod"

ENVIRONMENT_MAP = (LOCAL, DEV, STAGING, PROD)


def generate_random_string(length=30):
    return "".join(random.choices(ascii_letters + digits + punctuation, k=length))


def __verify_django_version():
    import django

    version = django.__version__
    print("Proceeding using django version: " + version)


def __verify_rest_framework_version():
    import rest_framework

    version = rest_framework.__version__
    print("Proceeding using rest_framework version: " + version)


def __verify_gunicorn_version():
    import gunicorn

    version = gunicorn.__version__
    print("Proceeding using gunicorn version: " + version)

def __verify_black_version():
    import black

    version = black.__version__
    print("Proceeding using black version: " + version)


def verify_or_install_django():
    try:
        __verify_django_version()
    except Exception as e:
        try:
            print(
                "Can't find django, attempting to install using `python3 -m pip install django`..."
            )

            pip.main(["install", "django"])
            __verify_django_version()
        except Exception as e:
            raise e


def verify_or_install_rest_framework():
    try:
        __verify_rest_framework_version()
    except Exception as e:
        try:
            print(
                "Can't find rest_framework, attempting to install using `python3 -m pip install djangorestframework`..."
            )

            pip.main(["install", "djangorestframework"])
            __verify_rest_framework_version()
        except Exception as e:
            raise e


def verify_or_install_gunicorn():
    try:
        __verify_gunicorn_version()
    except Exception as e:
        try:
            print(
                "Can't find gunicorn, attempting to install using `python3 -m pip install gunicorn`..."
            )

            pip.main(["install", "gunicorn"])
            __verify_gunicorn_version()
        except Exception as e:
            raise e

def verify_or_install_black():
    try:
        __verify_black_version()
    except Exception as e:
        try:
            print(
                "Can't find black, attempting to install using `python3 -m pip install black`..."
            )

            pip.main(["install", "black"])
            __verify_black_version()
        except Exception as e:
            raise e

def write_to_file(file_path, contents):
    if not os.path.exists(os.path.dirname(file_path)):
        try:
            os.makedirs(os.path.dirname(file_path))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    with open(file_path, "w") as out_file:
        out_file.write(contents)
