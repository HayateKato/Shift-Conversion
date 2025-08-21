"""Googleカレンダーとアプリケーション間のやり取りを行うモジュール"""

from google.oauth2 import service_account
from googleapiclient.discovery import build

from dataclass.shift import Shift

from unittest.mock import MagicMock, patch


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
