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

    def parse_data_to_shifts(result_dir: str) -> list[Shift]:
        """画像から抽出されたデータを使ってシフトデータを作成するメソッド
        Args:
            result_dir (str):画像や抽出結果ファイルを格納するディレクトリへのパス
        Returns:
            list[Shift]: シフトデータ
        """
        pass