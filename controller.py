"""アプリケーションを管理するモジュール"""

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
        shifts = self._image_processor.process_image(self.result_dir)
        self._calendar_client.create_events(shifts)
