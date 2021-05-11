from string import ascii_letters, digits, punctuation
import errno
import os
import random

DEFAULT_PATH = "../project_output"

DEFAULT_SERVICE_NAME = "django"

DEFAULT_PROJECT_NAME = "project"

DEFAULT_PROJECT_DIRECTORY = "project"

DEFAULT_SERVER_PORT = 8000

DEFAULT_DEBUG = True

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


def write_to_file(file_path, contents):
    if not os.path.exists(os.path.dirname(file_path)):
        try:
            os.makedirs(os.path.dirname(file_path))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    with open(file_path, "w") as out_file:
        out_file.write(contents)
