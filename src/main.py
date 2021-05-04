from utils import DEFAULT_PATH
from env_gen import EnvGen
from git_ignore_gen import GitIgnoreGen
from docker_gen import DockerGen
from nginx_gen import NginxGen

path = DEFAULT_PATH

EnvGen().generate_all_env_files(path=path)

GitIgnoreGen().generate_gitignore_file(path=path)

NginxGen().generate_nginx_files(path=path)

DockerGen().generate_docker_files(path=path)
