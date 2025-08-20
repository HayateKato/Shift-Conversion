"""画像処理とシフトデータの作成を行うモジュール"""

from image_processor.vision_client import VisionClient
from shift_parser import ShiftParser
from dataclass.shift import Shift


class ImageProcessor:
    """画像処理とシフトデータの作成を行うクラス
    Attributes:
        vision_client (:obj:`VisionClient`): Vision APIにおける処理を行うオブジェクト
        shift_parser (:obj:`ShiftParser`): 画像から抽出されたデータをシフトデータに変換するオブジェクト
    """

    def __init__(self):
        pass

    def process_image(result_dir: str) -> list[Shift]:
        """画像処理とシフトデータの作成を行うメソッド
        Args:
            result_dir (str):画像や抽出結果ファイルを格納するディレクトリへのパス
        Returns:
            list[Shift]: シフトデータ
        """
        pass
