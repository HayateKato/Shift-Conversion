"""アプリケーションで作成されたシフトデータを管理するモジュール
"""

import dataclasses


@dataclasses.dataclass
class Shift:
    """シフトデータを記録するクラス
    Attributes:
        subject (str): 予定の名前
        start_date (str): 予定の開始日
        start_time (str): 予定の開始時刻
        end_date (str): 予定の終了日
        end_time (str): 予定の終了時刻
    """
    subject: str
    start_date: str
    start_time: str
    end_date: str
    end_time: str