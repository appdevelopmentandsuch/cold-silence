from cold_silence.docker_gen import DockerGen
from cold_silence.env_gen import EnvGen
from cold_silence.git_ignore_gen import GitIgnoreGen
from cold_silence.nginx_gen import NginxGen
from pathlib import Path
from cold_silence.settings_gen import SettingsGen
from subprocess import Popen as pop
from cold_silence.utils import (
    DEFAULT_PATH,
    DEFAULT_SERVICE_NAME,
    DEFAULT_SERVER_PORT,
    DEFAULT_PROJECT_NAME,
    DEFAULT_PROJECT_DIRECTORY,
)
import argparse
import pip
import sys


def __verify_django_version():
    import django

    version = django.__version__
    print("Proceeding using Django version: " + version)


def __print_message(message, verbose):
    if verbose:
        print(message)


def __begin_gen_message(message, verbose):
    __print_message("Generating {0} ...".format(message), verbose=verbose)


def __end_gen_message(message, verbose):
    __print_message("{0} generated!".format(message), verbose=verbose)


def parse_args(args):
    print(args)
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

    verbose = args.verbose

    return {
        "path": path,
        "service_name": service_name,
        "server_port": server_port,
        "project_name": project_name,
        "project_directory": project_directory,
        "verbose": verbose,
    }


def generate_project(
    path=DEFAULT_PATH,
    service_name=DEFAULT_SERVICE_NAME,
    server_port=DEFAULT_SERVER_PORT,
    project_name=DEFAULT_PROJECT_NAME,
    project_directory=DEFAULT_PROJECT_DIRECTORY,
    verbose=False,
):
    try:
        __verify_django_version()
    except Exception as e:
        try:
            print(
                "Can't find Django, attempting to install using `python3 -m pip install django`..."
            )

            pip.main(["install", "django"])
            __verify_django_version()
        except Exception as e:
            print("Unable to install Django, install Django before proceeding.")
            exit(1)
    out_path = path

    __print_message("Creating directory " + out_path + " ...", verbose=verbose)

    Path(out_path).mkdir(parents=True, exist_ok=True)

    if not Path(out_path).exists:
        print("{0} was not created, exiting...")
        exit(1)

    __print_message(out_path + " created!", verbose=verbose)

    __begin_gen_message(
        "Django project " + project_name + " in " + out_path, verbose=verbose
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
        print(e)
        exit(1)

    __end_gen_message("Django project " + project_name, verbose=verbose)

    # Get inside the Django project's main directory
    settings_path = out_path + "/" + project_name + "/" + project_name

    __begin_gen_message("Settings file", verbose=verbose)

    SettingsGen().generate_settings_file(path=settings_path)

    __end_gen_message("Settings file", verbose=verbose)

    __begin_gen_message("Environment variable files", verbose=verbose)

    EnvGen().generate_all_env_files(path=path)

    __end_gen_message("Environment variable files", verbose=verbose)

    __begin_gen_message("Git ignore file", verbose=verbose)

    GitIgnoreGen().generate_gitignore_file(path=path)

    __end_gen_message("Git ignore file", verbose=verbose)

    __begin_gen_message("Nginx files", verbose=verbose)

    NginxGen().generate_nginx_files(
        path=path, server_port=server_port, service_name=service_name
    )

    __end_gen_message("Nginx files", verbose=verbose)

    __begin_gen_message("Dockerfiles and docker-compose files", verbose=verbose)

    DockerGen().generate_docker_files(
        path=path,
        project_directory=project_directory,
        project_name=project_name,
        server_port=server_port,
        service_name=service_name,
    )

    __end_gen_message("Dockerfiles and docker-compose files", verbose=verbose)

    print("Project generation complete, you're ready to get started!")
    print("Happy programming!")


def main():
    args = parse_args(sys.argv[1:])

    generate_project(
        path=args["path"],
        service_name=args["service_name"],
        server_port=args["server_port"],
        project_name=args["project_name"],
        project_directory=args["project_directory"],
        verbose=args["verbose"],
    )


if __name__ == "__main__":
    main()
