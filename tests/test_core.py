import unittest
import pathlib


class LgtmTest(unittest.TestCase):
    def test_lgtm(self):
        from lgtm.core import lgtm

        self.assertIsNone(lgtm("./python.jpeg", "LGTM"))
