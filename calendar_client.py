"""Googleカレンダーとアプリケーション間のやり取りを行うモジュール
"""

from dataclass.shift import Shift


class CalendarClient:
    """Googleカレンダーとアプリケーション間のやり取りを行うクラス
    Attributes:
        _api_key (str): Googleカレンダーを利用するための鍵のパス
        _calendar_id (str): 対象GoogleカレンダーのID
    """
    def __init__(self):
        pass

    def create_events(shift: list[Shift]) -> None:
        """Googleカレンダーにシフトデータを予定として追加するメソッド
        Args:
            shift (list[Shift]): シフトデータ
        Returns:
            None
        """