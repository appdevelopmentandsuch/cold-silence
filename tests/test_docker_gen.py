import unittest
import os
from cold_silence.docker_gen import DockerGen
from cold_silence.utils import DEFAULT_PATH, DEFAULT_PROJECT_DIRECTORY

class GitIgnoreTestSuite(unittest.TestCase):
    def test_create_gitignore(self):
        DockerGen().generate_docker_files()

        self.assertEqual(True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/" + DEFAULT_PROJECT_DIRECTORY + "/" + "Dockerfile")))
        self.assertEqual(True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/" + DEFAULT_PROJECT_DIRECTORY + "/" + "Dockerfile.prod")))
        self.assertEqual(True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/" + "docker-compose.yaml")))
