import unittest
import os
from cold_silence.utils import DEFAULT_PATH, write_to_file


class UtilsTestSuite(unittest.TestCase):
    def test_create_file(self):
        file_name = "file.txt"
        write_to_file(DEFAULT_PATH + "/" + file_name, "data")

        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/" + file_name))
        )
