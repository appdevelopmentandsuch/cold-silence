import unittest
import os
from cold_silence.settings_gen import SettingsGen
from cold_silence.utils import DEFAULT_PATH

class SettingsGenTestSuite(unittest.TestCase):
    def test_create_settings(self):
        SettingsGen().generate_settings_file()

        self.assertEqual(True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/settings.py")))
