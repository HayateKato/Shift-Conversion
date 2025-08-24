"""アプリケーションを管理するモジュール"""

import logging

from dataclass.file import File
from slack_client import SlackClient
from image_processor.image_processor import ImageProcessor
from calendar_client import CalendarClient


class Controller:
    """アプリケーションの管理を行うクラス
    Attributes:
        _slack_client(:obj:`SlackClient`): Slack関連の処理を行うオブジェクト
        _image_processor(:obj:`ImageProcessor`): 画像処理とシフトデータの作成を行うオブジェクト
        _calender_client(:obj:`CalenderClient`): シフトデータをGoogleカレンダーに追加するオブジェクト
        result_dir (str): 画像や抽出結果ファイルを格納するディレクトリへのパス
    """

    def __init__(self, result_dir: str):
        self._slack_client = SlackClient(controller=self)
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
        self._slack_client.listen_for_events()

    def handle_file_share_event(self, file: File) -> None:
        """クラス間でSlack上のファイル情報をやり取りするためのメソッド
        Args:
            file (:obj:`File`): Slack上のファイル情報
        Returns:
            None
        Notes:
            doctest対象外
        """
        # ログの設定
        logger = logging.getLogger("__main__").getChild("controller")
        logger.debug("バックグラウンド処理を開始しました。")

        # Slackに投稿された画像をローカルにダウンロード
        logger.debug("画像のダウンロードを開始しました。")
        self._slack_client.download_image(
            private_url=file.private_url, result_dir=self.result_dir
        )
        logger.debug("画像のダウンロードが完了しました。")

        # 画像ダウンロードの完了，シフトデータ作成の開始をSlack上で通知
        logger.debug("Slackへのメッセージ送信を開始しました。")
        self._slack_client.post_processing_message(file=file)
        logger.debug("Slackへのメッセージ送信が完了しました。")

        # シフトデータを作成
        logger.debug("シフトデータの作成を開始しました。")
        shifts = self._image_processor.process_image(result_dir=self.result_dir)
        logger.debug("シフトデータの作成が完了しました。")

        # シフトデータを予定としてGoogleカレンダーに追加
        logger.debug("Googleカレンダーへの予定の追加を開始しました。")
        self._calendar_client.create_events(shifts=shifts)
        logger.debug("Googleカレンダーへの予定の追加が完了しました。")

        # 作成したシフトデータをSlackに送信
        logger.debug("Slackへのシフトデータの送信を開始しました。")
        self._slack_client.post_result(file=file, shifts=shifts)
        logger.debug("Slackへのシフトデータの送信が完了しました。")

        logger.debug("バックグラウンド処理が完了しました。")
