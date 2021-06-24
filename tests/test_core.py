import unittest
import pathlib


class LgtmTest(unittest.TestCase):
    @unittest.skip("this is windows only")
    def test_lgtm(self):
        from lgtm.core import lgtm

        self.assertIsNone(lgtm("./python.jpg", "LGTM"))
