import requests
from io import BytesIO
from pathlib import Path


class LocalImage:
    """ローカルの画像ファイルを取得する"""

    # ファイルから画像を取得する

    def __init__(self, path):
        self.path = path

    def get_image(self):
        # 画像ファイルを読むときはバイナリで読む
        return open(self.path, mode="rb")


class RemoteImage:
    """URLから画像を取得する"""

    def __init__(self, path):
        self._url = path

    def get_image(self):

        data = requests.get(self._url)
        # byteデータをファイルオブジェクトに変換
        return BytesIO(data.content)


class _LoremFlickr(RemoteImage):
    """キーワード検索で画像を取得する
    URLで画像を取得するのでRemoteImageクラスを継承して使う
    """

    LOREM_FLICKER_URL = "https://loremflickr.com"
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, keyword):
        super().__init__(self._build_url(keyword))

    def _build_url(self, keyword):
        """キーワードからURLを組み立てて返す
        Returns:
            [URL]: https://loremflickr.com/WIDTH/HEIGHT/keyword/
        """
        return f"{self.LOREM_FLICKER_URL}/" f"{self.WIDTH}/{self.HEIGHT}/{keyword}"


# keyworkImageろいう別名で参照する
KeywordImage = _LoremFlickr

#
def ImageSource(keyword):
    """[keywordに基づいて最適なイメージクラスを返す]"""

    if keyword.startswith(("http://", "https://")):
        return RemoteImage(keyword)
    elif Path(keyword).exists():
        # ファイルやディレクトリの存在を確認できればローカルファイルのはず
        return LocalImage(keyword)
    else:
        return KeywordImage(keyword)


def get_image(keyword):
    """画像のファイルオブジェクトを返す"""
    return ImageSource(keyword).get_image()
