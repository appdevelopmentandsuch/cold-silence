from docker_gen import DockerGen
from env_gen import EnvGen
from git_ignore_gen import GitIgnoreGen
from nginx_gen import NginxGen
from settings_gen import SettingsGen
from subprocess import Popen as pop
from utils import (
    DEFAULT_PATH,
    DEFAULT_SERVICE_NAME,
    DEFAULT_SERVER_PORT,
    DEFAULT_PROJECT_NAME,
    DEFAULT_PROJECT_DIRECTORY,
)
import argparse
import os
import errno
import sys

parser = argparse.ArgumentParser()

parser.add_argument(
    "--path",
    help="Output path of the generated files, default is `../project_output`.",
    type=str,
)
parser.add_argument(
    "--service_name",
    help="Name of the containerized service, default is `project`.",
    type=str,
)
parser.add_argument(
    "--server_port",
    help="Port number of the containerized service, default is `8000`.",
    type=str,
)
parser.add_argument(
    "--project_name", help="Name of the project, default is `project`.", type=str
)
parser.add_argument(
    "--project_directory",
    help="Location of the project, default is `../project_output/project`.",
    type=str,
)

parser.add_argument("--verbose", help="Display verbose output", action="store_true")

args = parser.parse_args()

path = args.path if args.path is not None else DEFAULT_PATH
service_name = (
    args.service_name if args.service_name is not None else DEFAULT_SERVICE_NAME
)
server_port = args.server_port if args.server_port is not None else DEFAULT_SERVER_PORT
project_name = (
    args.project_name if args.project_name is not None else DEFAULT_PROJECT_NAME
)
project_directory = (
    args.project_directory
    if args.project_directory is not None
    else DEFAULT_PROJECT_DIRECTORY
)

try:
    import django

    version = django.__version__
    print("Proceeding using Django version: " + version)
except Exception as e:
    try:
        print(
            "Can't find Django, attempting to install using `python3 -m pip install django`..."
        )

        pop([sys.executable, "-m", "pip", "install", "django"], shell=False)

        import django

        version = django.__version__
        print("Proceeding using Django version: " + version)
    except Exception as e:
        print("Unable to install Django, install Django before proceeding.")
        exit(1)

out_path = path + "/" + project_name

if args.verbose:
    print("Creating directory " + out_path + " ...")

if not os.path.exists(os.path.dirname(out_path)):
        try:
            os.makedirs(os.path.dirname(out_path))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

if not os.path.exists(os.path.dirname(out_path)):
    print("{0} was not created, exiting...")
    exit(1)

if args.verbose:
    print(out_path + " created!")

if args.verbose:
    print("Generating Django project " + project_name + " in " + out_path + " ...")


pop(
    ["django-admin", "startproject", project_name,], shell=False, cwd=out_path
)

if args.verbose:
    print("Django project " + project_name + " generated!")

settings_path = out_path + "/" + project_name

if args.verbose:
    print("Generating settings file...")

SettingsGen().generate_settings_file(path=settings_path)

if args.verbose:
    print("Settings file generated!")


if args.verbose:
    print("Generating environment variable files...")

EnvGen().generate_all_env_files(path=path)

if args.verbose:
    print("Environment variable files generated!")

if args.verbose:
    print("Generating Git ignore file...")

GitIgnoreGen().generate_gitignore_file(path=path)

if args.verbose:
    print("Git ignore file generated!")

if args.verbose:
    print("Generating Nginx files...")

NginxGen().generate_nginx_files(
    path=path, server_port=server_port, service_name=service_name
)

if args.verbose:
    print("Nginx files generated!")

if args.verbose:
    print("Generating Dockerfiles and docker-compose files...")

DockerGen().generate_docker_files(
    path=path,
    project_directory=project_directory,
    project_name=project_name,
    server_port=server_port,
    service_name=service_name,
)


if args.verbose:
    print("Dockerfiles and docker-compose files generated!")

print("Project generation complete, you're ready to get started!")
print("Happy programming!")
