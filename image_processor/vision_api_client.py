"""Vision APIとアプリケーション間のやり取りを行うモジュール
"""

from google.cloud import vision
from google.cloud.vision import AnnotateImageResponse


class VisionAPIClient:
    """Vision APIを使って画像からデータを抽出するクラス
    Attributes:
        _api_key (str): Vision APIを利用するための鍵のパス
        _client (:obj:`google.cloud.vision_v1.ImageAnnotatorClient`)
    """
    def __init__(self):
        pass

    def extract_data_from_image(image_path: str) -> str:
        """画像からデータを抽出するメソッド
        Args:
            image_path (str): 処理を行う画像ファイルのパス
        Returns:
            str: 抽出されたデータファイルのパス
        """
        pass