"""アプリケーションを管理するモジュール
"""

from dataclass.file import File


class Controller:
    """アプリケーションの管理を行うクラス
    Attributes:
        slack_client(:obj:`SlackClient`): Slack関連の処理を行うオブジェクト
        image_processor(:obj:`ImageProcessor`): 画像処理とシフトデータの作成を行うオブジェクト
        calender_client(:obj:`CalenderClient`): シフトデータをGoogleカレンダーに追加するオブジェクト
    """
    def __init__(self):
        pass

    def run() -> None:
        """アプリケーションを起動するメソッド
        Args:
            None
        Returns:
            None
        """
        pass

    def handle_file_share_event(file: File) -> None:
        """クラス間でSlack上のファイル情報をやり取りするためのメソッド
        Args:
            file (:obj:`File`): Slack上のファイル情報
        Returns:
            None
        """
        pass
