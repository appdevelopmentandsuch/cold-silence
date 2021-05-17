from cold_silence.utils import (
    write_to_file,
    DEFAULT_PATH,
    DEFAULT_SERVICE_NAME,
    DEFAULT_SERVER_PORT,
)


class NginxGen:
    # Methods

    def __generate_nginx_dockerfile(self, path=DEFAULT_PATH):
        content = """
FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
        """

        write_to_file("{0}/nginx/Dockerfile".format(path), contents=content)

    def __generate_nginx_conf_file(
        self,
        path=DEFAULT_PATH,
        service_name=DEFAULT_SERVICE_NAME,
        server_port=DEFAULT_SERVER_PORT,
    ):
        content = """
upstream django {{
    server {0}:{1};
}}

server {{

    listen 80;

    location / {{
        proxy_pass http://django;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }}

}}
        """.format(
            service_name, server_port
        )

        write_to_file("{0}/nginx/nginx.conf".format(path), contents=content)

    def generate_nginx_files(
        self,
        path=DEFAULT_PATH,
        service_name=DEFAULT_SERVICE_NAME,
        server_port=DEFAULT_SERVER_PORT,
    ):
        self.__generate_nginx_conf_file(
            path=path, service_name=service_name, server_port=server_port
        )
        self.__generate_nginx_dockerfile(path=path)
