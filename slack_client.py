"""Slackとアプリケーション間のやり取りを行うモジュール
"""

from slack_bolt import App
from dataclass.file import File
from dataclass.shift import Shift
from unittest.mock import MagicMock, patch


class SlackClient:
    """Slackとアプリケーション間のやり取りを行うクラス
    Attributes:
        _bot_token (str): Slack Botのトークン
        _user_token (str): Slackユーザのトークン
        app (:obj:`Slack_bolt.app.app.App`)
    """
    def __init__(self):
        pass

    def listen_for_events(self) -> None:
        """Slackにおけるイベントの発生を検知するメソッド
        Args:
            None
        Returns:
            None
        Note:
            doctest対象外
        """
        pass

    def download_image(result_dir: str) -> None:
        """画像をローカルにダウンロードする関数
        Args:
            result_dir (str):画像や抽出結果ファイルを格納するディレクトリへのパス
        Returns:
            None
        """
        pass

    def send_result(self, file: File, shift: list[Shift]) -> None:
        """作成されたシフトデータをSlackに送信するメソッド
        Args:
            file (:obj:`File`): Slackにおける元ファイルの情報
            shift (list[Shift]): シフトデータ
        Returns:
            None
        Examples:
            >>> from slack_bolt import App
            >>> from dataclass.file import File
            >>> from dataclass.shift import Shift
            >>> from unittest.mock import MagicMock, patch
            >>> test_file = File(id="111", name="test.jpg", private_url="http://slack/test", channel_id="222", timestamp="2025-4-1 23:58:55.230456")
            >>> test_shifts = [Shift(subject="バイト", start_date="4/2/2025", start_time="17:00", end_date="4/2/2025", end_time="21:00"), Shift(subject="バイト", start_date="4/7/2025", start_time="19:00", end_date="4/7/2025", end_time="23:00")]
            >>> test_client = SlackClient()
            >>> with patch.object(test_client.app.client, "chat_postMessage") as mock_post:
            ...     test_client.send_result(test_file, test_shifts)
            >>> mock_post.assert_called_once()
            >>> test_text = "[バイト,4/2/2025,17:00,4/2/2025,21:00]\n[バイト,4/7/2025,19:00,4/7/2025,23:00]\n"
            >>> mock_post.assert_called_with(channel_id="222", text=test_text)
            >>> print("Test passed")
            Test passed
        """
        pass


    if __name__ == '__main__':
        import doctest
        doctest.testmod()