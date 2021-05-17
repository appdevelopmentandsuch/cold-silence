from cold_silence.docker_gen import DockerGen
from cold_silence.env_gen import EnvGen
from cold_silence.git_ignore_gen import GitIgnoreGen
from cold_silence.nginx_gen import NginxGen
from pathlib import Path
from cold_silence.settings_gen import SettingsGen
from cold_silence.requirements_gen import RequirementsGen
from subprocess import Popen as pop
from cold_silence.utils import (
    DEFAULT_PATH,
    DEFAULT_SERVICE_NAME,
    DEFAULT_SERVER_PORT,
    DEFAULT_PROJECT_NAME,
    DEFAULT_PROJECT_DIRECTORY,
    DEFAULT_CONFIG,
    ENGINE_SQLITE3,
    verify_or_install_django,
    verify_or_install_gunicorn,
    verify_or_install_rest_framework,
)
import argparse
import sys


def __print_message(message, verbose):
    if verbose:
        print(message)


def __begin_gen_message(message, verbose):
    __print_message("Generating {0} ...".format(message), verbose=verbose)


def __end_gen_message(message, verbose):
    __print_message("{0} generated!".format(message), verbose=verbose)


def parse_args(args):

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

    parser.add_argument(
        "--engine",
        help="Database to use for the project, the default is sqlite.",
        type=str,
    )

    parser.add_argument(
        "--rest_api",
        help="Generate a REST API starter, by default this is disabled",
        action="store_true",
    )

    parser.add_argument("--verbose", help="Display verbose output", action="store_true")

    args = parser.parse_args(args)

    path = args.path if args.path is not None else DEFAULT_PATH
    service_name = (
        args.service_name if args.service_name is not None else DEFAULT_SERVICE_NAME
    )
    server_port = (
        args.server_port if args.server_port is not None else DEFAULT_SERVER_PORT
    )
    project_name = (
        args.project_name if args.project_name is not None else DEFAULT_PROJECT_NAME
    )
    project_directory = (
        args.project_directory
        if args.project_directory is not None
        else DEFAULT_PROJECT_DIRECTORY
    )

    rest_api = args.rest_api if args.rest_api is not None else False

    engine = args.engine if args.engine is not None else ENGINE_SQLITE3

    verbose = args.verbose

    return {
        "engine": engine,
        "path": path,
        "project_directory": project_directory,
        "project_name": project_name,
        "rest_api": rest_api,
        "server_port": server_port,
        "service_name": service_name,
        "verbose": verbose,
    }


def generate_project(config=DEFAULT_CONFIG):
    verify_or_install_django()
    verify_or_install_gunicorn()
    verify_or_install_rest_framework()

    engine = config.get("engine", ENGINE_SQLITE3)
    out_path = config.get("path", DEFAULT_PATH)
    project_directory = config.get("project_directory", DEFAULT_PROJECT_DIRECTORY)
    project_name = config.get("project_name", DEFAULT_PROJECT_NAME)
    rest_api = config.get("rest_api", False)
    server_port = config.get("server_port", DEFAULT_SERVER_PORT)
    service_name = config.get("service_name", DEFAULT_SERVICE_NAME)
    verbose = config.get("verbose", False)

    __print_message("Creating directory " + out_path + " ...", verbose=verbose)

    Path(out_path).mkdir(parents=True, exist_ok=True)

    if not Path(out_path).exists:
        print("{0} was not created, exiting...")
        exit(1)

    __print_message(out_path + " created!", verbose=verbose)

    __begin_gen_message(
        "django project " + project_name + " in " + out_path, verbose=verbose
    )

    try:
        op = pop(
            ["/usr/bin/python3", "-m", "django", "startproject", project_name,],
            shell=False,
            cwd=out_path,
        )
        # https://stackoverflow.com/a/2837319
        op.communicate()
    except Exception as e:
        raise e

    __end_gen_message("django project " + project_name, verbose=verbose)

    # Get inside the django project's main directory
    settings_path = out_path + "/" + project_name + "/" + project_name

    __begin_gen_message("Settings file", verbose=verbose)

    SettingsGen().generate_settings_file(
        path=settings_path, project_name=project_name, engine=engine
    )

    __end_gen_message("Settings file", verbose=verbose)

    __begin_gen_message("Requirements file", verbose=verbose)

    RequirementsGen().generate_requirements_file(
        path=out_path, project_directory=project_directory
    )

    __end_gen_message("Requirements file", verbose=verbose)

    __begin_gen_message("Environment variable files", verbose=verbose)

    EnvGen().generate_all_env_files(path=out_path)

    __end_gen_message("Environment variable files", verbose=verbose)

    __begin_gen_message("Git ignore file", verbose=verbose)

    GitIgnoreGen().generate_gitignore_file(path=out_path)

    __end_gen_message("Git ignore file", verbose=verbose)

    __begin_gen_message("Nginx files", verbose=verbose)

    NginxGen().generate_nginx_files(
        path=out_path, server_port=server_port, service_name=service_name
    )

    __end_gen_message("Nginx files", verbose=verbose)

    __begin_gen_message("Dockerfiles and docker-compose files", verbose=verbose)

    DockerGen().generate_docker_files(
        path=out_path,
        project_directory=project_directory,
        project_name=project_name,
        server_port=server_port,
        service_name=service_name,
    )

    __end_gen_message("Dockerfiles and docker-compose files", verbose=verbose)

    print("Project generation complete, you're ready to get started!")
    print("Happy programming!")


def main():
    config = parse_args(sys.argv[1:])

    generate_project(config=config)


if __name__ == "__main__":
    main()
