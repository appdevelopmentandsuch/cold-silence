from utils import (
    DEFAULT_PATH,
    DEFAULT_SERVICE_NAME,
    DEFAULT_SERVER_PORT,
    DEFAULT_PROJECT_NAME,
    DEFAULT_PROJECT_DIRECTORY,
)
from env_gen import EnvGen
from git_ignore_gen import GitIgnoreGen
from docker_gen import DockerGen
from nginx_gen import NginxGen
import argparse

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

EnvGen().generate_all_env_files(path=path)

GitIgnoreGen().generate_gitignore_file(path=path)

NginxGen().generate_nginx_files(
    path=path, server_port=server_port, service_name=service_name
)

DockerGen().generate_docker_files(
    path=path,
    project_directory=project_directory,
    project_name=project_name,
    server_port=server_port,
    service_name=service_name,
)
