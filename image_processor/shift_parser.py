"""画像から抽出されたデータをシフトデータに変換するモジュール
"""

from dataclass.shift import Shift


class ShiftParser:
    """画像から抽出されたデータをシフトデータに変換するモジュール
    Attributes:
        None
    """
    def __init__(self):
        pass

    def parse_data_to_shifts(raw_data_path: str) -> list[Shift]:
        """画像から抽出されたデータを使ってシフトデータを作成するメソッド
        Args:
            raw_data_path (str): 画像から抽出されたデータのパス
        Returns:
            list[Shift]: シフトデータ
        """
        pass