from utils import (
    write_to_file,
    DEFAULT_PATH,
    DEFAULT_PROJECT_DIRECTORY,
    DEFAULT_PROJECT_NAME,
    DEFAULT_SERVICE_NAME,
    DEFAULT_SERVER_PORT,
)


class DockerGen:
    # Methods

    def __generate_docker_compose(
        self,
        path=DEFAULT_PATH,
        service_name=DEFAULT_SERVICE_NAME,
        project_directory=DEFAULT_PROJECT_DIRECTORY,
        project_name=DEFAULT_PROJECT_NAME,
        server_port=DEFAULT_SERVER_PORT,
    ):
        content = """
version: '2'

services:
nginx:
    build: ./nginx
    ports:
    - 80:80
    depends_on:
    - {0}
{0}:
    build: ./{1}
    command: gunicorn {2}.wsgi:application --bind 0.0.0.0:{3}
    expose:
    - {3}
        """.format(
            service_name, project_directory, project_name, server_port
        )

        write_to_file("{0}/docker-compose.yaml".format(path), contents=content)

    def __generate_django_dockerfile(
        self, path=DEFAULT_PATH, project_directory=DEFAULT_PROJECT_DIRECTORY
    ):
        content = """
FROM python:3.8-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
        """

        write_to_file(
            "{0}/{1}/Dockerfile".format(path, project_directory), contents=content
        )

    def generate_docker_files(
        self,
        path=DEFAULT_PATH,
        service_name=DEFAULT_SERVICE_NAME,
        project_directory=DEFAULT_PROJECT_DIRECTORY,
        project_name=DEFAULT_PROJECT_NAME,
        server_port=DEFAULT_SERVER_PORT,
    ):
        self.__generate_django_dockerfile(
            path=path, project_directory=project_directory
        )
        self.__generate_docker_compose(
            path=path,
            service_name=service_name,
            project_directory=project_directory,
            project_name=project_name,
            server_port=server_port,
        )
