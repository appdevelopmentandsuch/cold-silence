from cold_silence.utils import (
    DEFAULT_PROJECT_DIRECTORY,
    write_to_file,
    DEFAULT_PATH,
)


class RequirementsGen:
    # Methods
    def __generate_rest_api_requirements_file_content(self):
        try:
            import rest_framework
        except Exception as e:
            raise e

        return "djangorestframework=={0}".format(rest_framework.__version__)

    def __generate_standard_requirements_file_content(self):
        try:
            import django
            import gunicorn
        except Exception as e:
            raise e

        return """
Django=={0}
gunicorn=={1}
""".format(
            django.__version__, gunicorn.__version__
        )

    def generate_requirements_file(
        self,
        path=DEFAULT_PATH,
        project_directory=DEFAULT_PROJECT_DIRECTORY,
        rest_api=False,
    ):
        content = self.__generate_standard_requirements_file_content()

        if rest_api:
            rest_content = self.__generate_rest_api_requirements_file_content()
            content += "\n{0}".format(rest_content)

        write_to_file(
            "{0}/{1}/requirements.txt".format(path, project_directory), contents=content
        )
