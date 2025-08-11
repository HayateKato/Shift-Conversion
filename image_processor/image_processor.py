"""画像処理とシフトデータの作成を行うモジュール
"""

from vision_api_client import VisionAPIClient
from shift_parser import ShiftParser
from ..dataclass.shift import Shift


class ImageProcessor:
    """画像処理とシフトデータの作成を行うクラス
    Attributes:
        vision_api_client (:obj:`VisionAPIClient`): Vision APIにおける処理を行うオブジェクト
        shift_parser (:obj:`ShiftParser`): 画像から抽出されたデータをシフトデータに変換するオブジェクト
    """
    def __init__(self):
        pass

    def process_image(image_path: str) -> list[Shift]:
        """画像処理とシフトデータの作成を行うメソッド
        Args:
            image_path (str): 処理を行う画像ファイルのパス
        Returns:
            list[Shift]: シフトデータ
        """
        pass