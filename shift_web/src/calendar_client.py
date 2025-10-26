"""Googleカレンダーとアプリケーション間のやり取りを行うモジュール"""

from dotenv import load_dotenv
import os

load_dotenv("src/.env")
from google.oauth2 import service_account
import googleapiclient.discovery

from src.dataclass.shift import Shift

from unittest.mock import MagicMock, patch


class CalendarClient:
    """Googleカレンダーとアプリケーション間のやり取りを行うクラス
    Attributes:
        _api_key (str): Googleカレンダーを利用するための鍵のパス
        _calendar_id (str): 対象GoogleカレンダーのID
        _creds (:obj:`google.oauth2.service_account.Credentials`): 認証情報
        _service (:obj:`googleapiclient.discovery.Resource`): Googleカレンダーとのやりとりを担うオブジェクト
    """

    def __init__(self):
        self._api_key = os.getenv("GOOGLE_CLOUD_API_KEY_PATH")
        self._calendar_id = os.getenv("GOOGLE_CALENDAR_ID")
        self._creds = service_account.Credentials.from_service_account_file(
            self._api_key
        )
        self._service = googleapiclient.discovery.build(
            "calendar", "v3", credentials=self._creds
        )

    def create_events(self, shifts: list[Shift]) -> None:
        """Googleカレンダーにシフトデータを予定として追加するメソッド
        Args:
            shift (list[Shift]): シフトデータ
        Returns:
            None
        Examples:
            >>> from unittest.mock import patch, MagicMock, call
            >>> from dataclass.shift import Shift
            >>>
            >>> # --- 1. ダミーデータの設定 ---
            >>> dummy_key_path = "dummy/key.json"
            >>> dummy_calendar_id = "dummy@outlook.jp"
            >>> dummy_shifts = [
            ...     Shift(summary="バイト", start_datetime="2025-04-02T17:00:00+09:00:00", end_datetime="2025-04-02T21:30:00+09:00:00", timezone="Asia/Tokyo"),
            ...     Shift(summary="バイト", start_datetime="2025-04-04T17:00:00+09:00:00", end_datetime="2025-04-04T21:00:00+09:00:00", timezone="Asia/Tokyo")
            ... ]
            >>> dummy_shifts_dict = [
            ...     {"summary":"バイト", "start_datetime":"2025-04-02T17:00:00+09:00:00", "end_datetime":"2025-04-02T21:30:00+09:00:00", "timezone":"Asia/Tokyo"},
            ...     {"summary":"バイト", "start_datetime":"2025-04-04T17:00:00+09:00:00", "end_datetime":"2025-04-04T21:00:00+09:00:00", "timezone":"Asia/Tokyo"}
            ... ]
            >>>
            >>> # --- 2. 外部依存のモック化とテスト実行 ---
            >>> # __init__で呼ばれる関数をまとめてモック化
            >>> with patch("os.getenv") as mock_getenv, \\
            ...      patch("google.oauth2.service_account.Credentials.from_service_account_file") as mock_from_file, \\
            ...      patch("googleapiclient.discovery.build") as mock_build, \\
            ...      patch("__main__.Shift.to_dict") as mock_to_dict:
            ...
            ...     # --- モックの設定 ---
            ...     mock_getenv.side_effect = [dummy_key_path, dummy_calendar_id]
            ...     # build関数が返すサービスオブジェクトをMagicMockで作成
            ...     mock_service = MagicMock()
            ...     mock_build.return_value = mock_service
            ...     mock_to_dict.side_effect = dummy_shifts_dict
            ...
            ...     # --- テスト対象の実行 ---
            ...     test_client = CalendarClient()
            ...     test_client.create_events(shifts=dummy_shifts)
            ...
            >>> # --- 検証 ---
            >>> mock_from_file.assert_called_once_with(dummy_key_path)
            >>>
            >>> assert mock_to_dict.call_count == 2
            >>>
            >>> # insertメソッドが正しい引数で呼ばれたかを検証
            >>> expected_calls = [
            ...     call(calendarId=dummy_calendar_id, body={"summary": "バイト", "start": {"dateTime": "2025-04-02T17:00:00+09:00:00", "timeZone": "Asia/Tokyo"}, "end": {"dateTime": "2025-04-02T21:30:00+09:00:00", "timeZone": "Asia/Tokyo"}}),
            ...     call(calendarId=dummy_calendar_id, body={"summary": "バイト", "start": {"dateTime": "2025-04-04T17:00:00+09:00:00", "timeZone": "Asia/Tokyo"}, "end": {"dateTime": "2025-04-04T21:00:00+09:00:00", "timeZone": "Asia/Tokyo"}}),
            ... ]
            >>>
            >>> # 実際に呼ばれた内容が期待通りかを確認
            >>> assert mock_service.events().insert.call_args_list == expected_calls
            >>>
            >>> # execute()も2回呼ばれたことを確認
            >>> assert mock_service.events().insert().execute.call_count == 2
        """
        for shift in shifts:
            shift_dict = shift.to_dict()
            event = {
                "summary": shift_dict["summary"],
                "start": {
                    "dateTime": shift_dict["start_datetime"],
                    "timeZone": shift_dict["timezone"],
                },
                "end": {
                    "dateTime": shift_dict["end_datetime"],
                    "timeZone": shift_dict["timezone"],
                },
            }
            self._service.events().insert(
                calendarId=self._calendar_id, body=event
            ).execute()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
