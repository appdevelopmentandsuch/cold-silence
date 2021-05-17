from cold_silence.main import generate_project, parse_args
from cold_silence.utils import DEFAULT_PATH, DEFAULT_PROJECT_DIRECTORY
import os
import unittest


class MainTestSuite(unittest.TestCase):
    def test_create_project(self):

        generate_project()

        self.assertEqual(
            True,
            os.path.exists(
                os.path.dirname(
                    DEFAULT_PATH + "/" + DEFAULT_PROJECT_DIRECTORY + "/" + "Dockerfile"
                )
            ),
        )
        self.assertEqual(
            True,
            os.path.exists(
                os.path.dirname(
                    DEFAULT_PATH
                    + "/"
                    + DEFAULT_PROJECT_DIRECTORY
                    + "/"
                    + "Dockerfile.prod"
                )
            ),
        )
        self.assertEqual(
            True,
            os.path.exists(os.path.dirname(DEFAULT_PATH + "/" + "docker-compose.yaml")),
        )
        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/nginx/Dockerfile"))
        )
        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/nginx/nginx.conf"))
        )
        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/settings.py"))
        )
        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/.gitignore"))
        )
        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/local.env"))
        )
        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/dev.env"))
        )
        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/staging.env"))
        )
        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/prod.env"))
        )

    def test_create_project_from_main(self):

        config = parse_args(
            [
                "--server_port",
                "8080",
                "--project_name",
                "my_project",
                "--service_name",
                "my_service",
                "--project_directory",
                "my_project",
                "--verbose",
            ]
        )

        generate_project(config=config)

        self.assertEqual(
            True,
            os.path.exists(
                os.path.dirname(
                    DEFAULT_PATH + "/" + DEFAULT_PROJECT_DIRECTORY + "/" + "Dockerfile"
                )
            ),
        )
        self.assertEqual(
            True,
            os.path.exists(
                os.path.dirname(
                    DEFAULT_PATH
                    + "/"
                    + DEFAULT_PROJECT_DIRECTORY
                    + "/"
                    + "Dockerfile.prod"
                )
            ),
        )
        self.assertEqual(
            True,
            os.path.exists(os.path.dirname(DEFAULT_PATH + "/" + "docker-compose.yaml")),
        )
        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/nginx/Dockerfile"))
        )
        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/nginx/nginx.conf"))
        )
        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/settings.py"))
        )
        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/.gitignore"))
        )
        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/local.env"))
        )
        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/dev.env"))
        )
        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/staging.env"))
        )
        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/prod.env"))
        )
