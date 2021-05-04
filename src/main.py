from env_gen import EnvGen
from git_ignore_gen import GitIgnoreGen

envs = EnvGen().ENVIRONMENT_MAP

for env in envs:
    EnvGen().write_env_file(env)

GitIgnoreGen().write_git_ignore()
