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
        Examples:
            >>> dummy_shift = Shift(summary="バイト", start_datetime="2025-04-02T17:00:00+09:00:00", end_datetime="2025-04-02T21:30:00+09:00:00", timezone="Asia/Tokyo")
            >>> dummy_shift.to_dict()
            {'summary': 'バイト', 'start_datetime': '2025-04-02T17:00:00+09:00:00', 'end_datetime': '2025-04-02T21:30:00+09:00:00', 'timezone': 'Asia/Tokyo'}
        """
        shift_dict = {"summary": self.summary, "start_datetime": self.start_datetime, "end_datetime": self.end_datetime, "timezone": self.timezone}

        return shift_dict


if __name__ == "__main__":
    import doctest

    doctest.testmod()
