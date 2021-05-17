import unittest
import os
from cold_silence.utils import DEFAULT_PATH, DEFAULT_PROJECT_DIRECTORY
from cold_silence.main import generate_project


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

    def test_create_verbose_project(self):

        generate_project(verbose=True)

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
