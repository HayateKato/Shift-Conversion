"""Slackとアプリケーション間のやり取りを行うモジュール
"""

from slack_bolt import App
from dataclass.file import File
from dataclass.shift import Shift


class SlackClient:
    """Slackとアプリケーション間のやり取りを行うクラス
    Attributes:
        _bot_token (str): Slack Botのトークン
        _user_token (str): Slackユーザのトークン
        app (:obj:`Slack_bolt.app.app.App`)
    """
    def __init__(self):
        pass

    def listen_for_events() -> None:
        """Slackにおけるイベントの発生を検知するメソッド
        Args:
            None
        Returns:
            None
        """
        pass

    def send_result(file: File, shift: list[Shift]) -> None:
        """作成されたシフトデータをSlackに送信するメソッド
        Args:
            file (:obj:`File`): Slackにおける元ファイルの情報
            shift (list[Shift]): シフトデータ
        Returns:
            None
        """
        pass