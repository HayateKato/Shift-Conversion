"""アプリケーションで作成されたシフトデータを管理するモジュール
"""

import dataclasses


@dataclasses.dataclass
class Shift:
    """シフトデータを記録するクラス
    Attributes:
        summary (str): 予定の名前
        start_datetime (str): 予定の開始日時
        end_datetime (str): 予定の終了日時
        timezone (str): タイムゾーン
    """
    summary: str
    start_datetime: str
    end_datetime: str
    timezone: str

    def to_dict(self) -> dict:
        """シフト情報を辞書型に変換するメソッド
        Args:
            None
        Returns:
            dict: 辞書型シフトデータ
        """
        pass