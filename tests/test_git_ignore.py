import unittest
import os
from cold_silence.git_ignore_gen import GitIgnoreGen
from cold_silence.utils import DEFAULT_PATH


class GitIgnoreGenTestSuite(unittest.TestCase):
    def test_create_gitignore(self):
        GitIgnoreGen().generate_gitignore_file(path=DEFAULT_PATH)

        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/.gitignore"))
        )
