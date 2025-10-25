"""アプリケーションを管理するモジュール"""

import logging

from src.image_processor.image_processor import ImageProcessor
from src.calendar_client import CalendarClient


class Controller:
    """アプリケーションの管理を行うクラス
    Attributes:
        _image_processor(:obj:`ImageProcessor`): 画像処理とシフトデータの作成を行うオブジェクト
        _calender_client(:obj:`CalenderClient`): シフトデータをGoogleカレンダーに追加するオブジェクト
        result_dir (str): 画像や抽出結果ファイルを格納するディレクトリへのパス
    """

    def __init__(self, result_dir: str):
        self._image_processor = ImageProcessor()
        self._calendar_client = CalendarClient()
        self.result_dir = result_dir

    def run(self) -> None:
        """アプリケーションを起動するメソッド
        Args:
            None
        Returns:
            None
        Notes:
            doctest対象外
        """
        # ログの設定
        logger = logging.getLogger("__main__").getChild("controller")
        logger.debug("バックグラウンド処理を開始しました。")

        # シフトデータを作成
        logger.debug("シフトデータの作成を開始しました。")
        shifts = self._image_processor.process_image(result_dir=self.result_dir)
        logger.debug("シフトデータの作成が完了しました。")

        # シフトデータを予定としてGoogleカレンダーに追加
        logger.debug("Googleカレンダーへの予定の追加を開始しました。")
        self._calendar_client.create_events(shifts=shifts)
        logger.debug("Googleカレンダーへの予定の追加が完了しました。")

        logger.debug("バックグラウンド処理が完了しました。")
