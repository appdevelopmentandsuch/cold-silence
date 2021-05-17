import unittest
import os
from cold_silence.env_gen import EnvGen
from cold_silence.utils import DEFAULT_PATH


class EnvGenTestSuite(unittest.TestCase):
    def test_create_envs(self):
        EnvGen().generate_all_env_files()

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
