import unittest
import os
from cold_silence.nginx_gen import NginxGen
from cold_silence.utils import DEFAULT_PATH


class NginxGenTestSuite(unittest.TestCase):
    def test_create_nginx(self):
        NginxGen().generate_nginx_files()

        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/nginx/Dockerfile"))
        )
        self.assertEqual(
            True, os.path.exists(os.path.dirname(DEFAULT_PATH + "/nginx/nginx.conf"))
        )
