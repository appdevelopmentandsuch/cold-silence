from utils import (
    generate_random_string,
    write_to_file,
    DEFAULT_PATH,
    LOCAL,
    DEV,
    STAGING,
    PROD,
    ENVIRONMENT_MAP,
)


class EnvGen:

    # Variables
    SECRET_KEY = "SECRET_KEY"
    DEBUG = "DEBUG"
    ALLOWED_HOSTS = "ALLOWED_HOSTS"

    ENVIRONMENT_VARIABLE_MAP = {
        LOCAL: {
            SECRET_KEY: generate_random_string,
            DEBUG: True,
            ALLOWED_HOSTS: "localhost,127.0.0.1",
        },
        DEV: {SECRET_KEY: generate_random_string, DEBUG: True, ALLOWED_HOSTS: "",},
        STAGING: {SECRET_KEY: generate_random_string, DEBUG: False, ALLOWED_HOSTS: "",},
        PROD: {SECRET_KEY: generate_random_string, DEBUG: False, ALLOWED_HOSTS: "",},
    }

    # Methods

    def __create_environemt_variable(self, variable, value=generate_random_string):
        return "export {0}={2}{1}{2}\n".format(
            variable,
            value() if callable(value) else value,
            '"' if not isinstance(value, bool) else "",
        )

    def __generate_env_file(self, environment, path=DEFAULT_PATH):
        variables = self.ENVIRONMENT_VARIABLE_MAP[environment]

        content = "".join(
            self.__create_environemt_variable(variable=key, value=value)
            for key, value in variables.items()
        )

        write_to_file("{0}/{1}.env".format(path, environment), contents=content)

    def generate_all_env_files(self, path=DEFAULT_PATH):
        envs = ENVIRONMENT_MAP

        for env in envs:
            self.__generate_env_file(env, path)
