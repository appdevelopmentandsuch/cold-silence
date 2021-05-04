from string import ascii_letters, digits, punctuation
import errno
import os
import random

DEFAULT_PATH = "../project_output"

DEFAULT_SERVICE_NAME = "django"

DEFAULT_PROJECT_NAME = "project"

DEFAULT_PROJECT_DIRECTORY = "project"

DEFAULT_SERVER_PORT = 8000


def generate_random_string(length=30):
    return "".join(random.choices(ascii_letters + digits + punctuation, k=length))


def write_to_file(file_path, contents):
    if not os.path.exists(os.path.dirname(file_path)):
        try:
            os.makedirs(os.path.dirname(file_path))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    out_file = open(file_path, "w")

    out_file.write(contents)

    out_file.close()
