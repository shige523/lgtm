import unittest
import pathlib
import os
from tempfile import TemporaryFile


class ImageSourceTest(unittest.TestCase):
    def setUp(self):
        # 一時ファイルを作成する
        self.file01 = pathlib.Path("./book.jpeg")
        self.file01.touch()

    def tearDown(self):

        self.file01.unlink()

    def test_remote_image(self):
        from lgtm.image_source import ImageSource, RemoteImage

        self.assertIsInstance(ImageSource("http://test"), RemoteImage)
        # self.assertIs(type(ImageSource("http://test")), RemoteImage)

    def test_keyword_image(self):
        from lgtm.image_source import ImageSource, KeywordImage

        self.assertIsInstance(ImageSource("book"), KeywordImage)

    def test_localfile_image(self):
        from lgtm.image_source import ImageSource, LocalImage

        self.assertIsInstance(ImageSource("./book.jpeg"), LocalImage)
