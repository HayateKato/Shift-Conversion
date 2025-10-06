"""Slackとアプリケーション間のやり取りを行うモジュール"""

from dotenv import load_dotenv
import os

load_dotenv("/src/.env")
import requests
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from dataclass.file import File
from dataclass.shift import Shift

# typingからTYPE_CHECKINGをインポート
from typing import TYPE_CHECKING

# Controllerを直接インポートする代わりにTYPE_CHECKINGブロックの中でだけインポートする
if TYPE_CHECKING:
    from controller import Controller

from unittest.mock import MagicMock, patch


class SlackClient:
    """Slackとアプリケーション間のやり取りを行うクラス
    Attributes:
        _bot_token (str): Slack Botのトークン
        _socket_token (str): Slackのソケットモードを使うためのトークン
        _app (:obj:`Slack_bolt.app.app.App`)
        _controller (:obj:`Controller`): Controllerクラスのオブジェクト
    """

    def __init__(self, controller: "Controller"):
        self._bot_token = os.getenv("SLACK_BOT_OAUTH_TOKEN")
        self._socket_token = os.getenv("SLACK_SOKET_TOKEN")
        self._app = App(token=self._bot_token)
        self._controller = controller
        self._regist_handlers()

    def _regist_handlers(self) -> None:
        """Slack上のイベントを管理するメソッド
        Slack上に画像が投稿されると実行される
        Args:
            None
        Returns:
            None
        Notes:
            doctest対象外
        """

        @self._app.event({"type": "message", "subtype": "file_share"})
        def _handle_event(event: dict) -> None:
            """Slack上に画像が投稿されると実行されるメソッド
            _process_file_share_eventメソッドを呼び出す
            Args:
                event (dict): Slackから送られてくるイベントの情報
            Returns:
                None
            Notes:
                doctest対象外
            """
            self._process_file_share_event(event)

    def _process_file_share_event(self, event: dict) -> None:
        """Slack上に投稿された画像の情報をFileオブジェクトに変換してControllerクラスに渡すメソッド
        Args:
            event (dict): Slackから送られてくるイベントの情報
        Returns:
            None
        Examples:
            >>> # --- 1. テストの準備 ---
            >>> from unittest.mock import MagicMock, patch
            >>>
            >>> # テスト用のダミーを作成
            >>> mock_controller = MagicMock()
            >>> # Slack APIの仕様に合わせたイベントデータ
            >>> test_event = {
            ...     "type": "message",
            ...     "files": [{
            ...         "id": "F0RDC39U1",
            ...         "name": "ghostrap.png",
            ...         "url_private": "https://files.slack.com/files-pri/T061EG9R6-F0RDC39U1/ghostrap.png"
            ...     }],
            ...     "channel": "D0L4B9P0Q",
            ...     "event_ts": "1529342088.000086"
            ... }
            >>>
            >>> # --- 2. 外部依存をモック化してテストを実行 ---
            >>> # `os.getenv` と `App` をモック化して、__init__がエラーにならないようにする
            >>> with patch('os.getenv', return_value='dummy-token'):
            ...     with patch('__main__.App') as MockApp:
            ...         # --- モックの設定 ---
            ...         mock_app_instance = MockApp.return_value    # self._app == mock_app_instanceとなるようにする
            ...
            ...         # --- テスト対象の実行 ---
            ...         test_client = SlackClient(controller=mock_controller)
            ...         # テスト対象のロジックメソッドを直接呼び出す
            ...         test_client._process_file_share_event(test_event)
            ...
            >>> # --- 3. 結果の検証 ---
            >>> # Controllerのメソッドが1回だけ呼ばれたことを確認
            >>> mock_controller.handle_file_share_event.assert_called_once()
            >>>
            >>> # Controllerに渡されたFileオブジェクトの属性が正しいかを確認
            >>> # call_args[0][0] で、呼び出し時の最初の引数(Fileオブジェクト)を取得
            >>> called_file_obj = mock_controller.handle_file_share_event.call_args[0][0]
            >>> assert called_file_obj.id == "F0RDC39U1"
            >>> assert called_file_obj.name == "ghostrap.png"
            >>> assert called_file_obj.private_url == "https://files.slack.com/files-pri/T061EG9R6-F0RDC39U1/ghostrap.png"
            >>> assert called_file_obj.channel_id == "D0L4B9P0Q"
            >>> assert called_file_obj.timestamp == "1529342088.000086"
        """
        file_obj = File(
            id=event["files"][0]["id"],
            name=event["files"][0]["name"],
            private_url=event["files"][0]["url_private"],
            channel_id=event["channel"],
            timestamp=event["event_ts"],
        )
        self._controller.handle_file_share_event(file_obj)

    def listen_for_events(self) -> None:
        """Slackにおけるイベントの発生を検知するメソッド
        Args:
            None
        Returns:
            None
        Note:
            doctest対象外
        """
        handler = SocketModeHandler(self._app, self._socket_token)
        handler.start()

    def download_image(self, private_url: str, result_dir: str) -> None:
        """画像をローカルにダウンロードするメソッド
        Args:
            private_url (str): Slack上にアップロードされた画像のURL
            result_dir (str): 画像や抽出結果ファイルを格納するディレクトリへのパス
        Returns:
            None
        Examples:
            >>> # --- 1. テストの準備 ---
            >>> from unittest.mock import MagicMock, patch, mock_open
            >>>
            >>> # テスト用のダミーを作成
            >>> mock_controller = MagicMock()
            >>> test_private_url = "http://slack/test"
            >>> test_result_dir = "result/dummy"
            >>> dummy_bot_token = "dummy-token"
            >>>
            >>> # --- 2. 外部依存をモック化してテストを実行 ---
            >>> # `os.getenv` をモック化して、__init__がエラーにならないようにする
            >>> with patch("os.getenv", return_value=dummy_bot_token):
            ...     # `App` の初期化をモック化
            ...     with patch("__main__.App") as MockApp:
            ...         # `requests.get`をモック化
            ...         with patch("requests.get") as mock_get:
            ...             # `builtins.open`をモック化
            ...             with patch("builtins.open", mock_open()) as mock_file:
            ...                 # --- モックの設定 ---
            ...                 mock_app_instance = MockApp.return_value    # self._app == mock_app_instanceとなるようにする
            ...                 mock_response = MagicMock()
            ...                 mock_response.content = b"dummy image data"
            ...                 mock_get.return_value = mock_response
            ...
            ...                 # --- テスト対象の実行 ---
            ...                 test_client = SlackClient(controller=mock_controller)
            ...                 test_client._bot_token = dummy_bot_token
            ...                 test_client.download_image(test_private_url, test_result_dir)
            ...
            >>> # --- 3. 結果の検証 ---
            >>> # 1回だけ呼ばれたことを確認
            >>> mock_get.assert_called_once()
            >>>
            >>> # 正しい引数で呼ばれたかを確認
            >>> mock_get.assert_called_with(url=test_private_url, allow_redirects=True, headers={"Authorization": f"Bearer {dummy_bot_token}"}, stream=True)
            >>>
            >>> # 正しいファイル処理が行われようとしたか確認
            >>> mock_file.assert_any_call(f"{test_result_dir}/shift.jpg", "wb")
            >>> file_handle = mock_file()
            >>> file_handle.write.assert_called_once_with(b"dummy image data")
        """
        img_data = requests.get(
            url=private_url,
            allow_redirects=True,
            headers={"Authorization": f"Bearer {self._bot_token}"},
            stream=True,
        ).content
        with open(f"{result_dir}/shift.jpg", "wb") as f:
            f.write(img_data)

    def post_processing_message(self, file: File) -> str:
        """ローカルへの画像のダウンロードの完了とシフト変換の開始を通知するメソッド
        Args:
            file (:obj:`File`): Slackにおける元ファイルの情報
        Returns:
            str: 投稿されたメッセージのタイムスタンプ
        Exaples:
            >>> # --- 1. テストの準備 ---
            >>> from dataclass.file import File
            >>> from dataclass.shift import Shift
            >>> from unittest.mock import MagicMock, patch
            >>>
            >>> # テスト用のダミーを作成
            >>> mock_controller = MagicMock()
            >>> test_file = File(id="F111", name="test.jpg", private_url="http://slack/test", channel_id="C222", timestamp="1648825135.123")
            >>>
            >>> # --- 2. 外部依存をモック化してテストを実行 ---
            >>> # `os.getenv` をモック化して、__init__がエラーにならないようにする
            >>> with patch("os.getenv", return_value="dummy-token"):
            ...     # `App` の初期化をモック化
            ...     with patch("__main__.App") as MockApp:
            ...         # --- モックの設定 ---
            ...         # Appインスタンスが持つclientのchat_postMessageをモック化
            ...         mock_app_instance = MockApp.return_value    # self._app == mock_app_instanceとなるようにする
            ...         mock_post = mock_app_instance.client.chat_postMessage
            ...
            ...         # --- テスト対象の実行 ---
            ...         test_client = SlackClient(controller=mock_controller)
            ...         _ = test_client.post_processing_message(test_file)
            ...
            >>> # --- 3. 結果の検証 ---
            >>> # 1回だけ呼ばれたことを確認
            >>> mock_post.assert_called_once()
            >>>
            >>> # 正しい引数で呼ばれたかを確認
            >>> expected_text = "画像のダウンロードが完了しました。\\n 処理中です..."
            >>> mock_post.assert_called_with(channel="C222", thread_ts="1648825135.123", text=expected_text)
        """
        channel = file.channel_id
        timestamp = file.timestamp
        text = "画像のダウンロードが完了しました。\n処理中です．．．"
        response = self._app.client.chat_postMessage(
            channel=channel, thread_ts=timestamp, text=text
        )

        return response["ts"]

    def post_result(self, file: File, shifts: list[Shift]) -> None:
        """作成されたシフトデータをSlackに送信するメソッド
        Args:
            file (:obj:`File`): Slackにおける元ファイルの情報
            shift (list[Shift]): シフトデータ
        Returns:
            None
        Examples:
            >>> # --- 1. テストの準備 ---
            >>> from dataclass.file import File
            >>> from dataclass.shift import Shift
            >>> from unittest.mock import MagicMock, patch
            >>>
            >>> # テスト用のダミーを作成
            >>> mock_controller = MagicMock()
            >>> test_file = File(id="F111", name="test.jpg", private_url="http://slack/test", channel_id="C222", timestamp="1648825135.123")
            >>> test_shifts = [Shift(summary="バイト", start_datetime="2025-04-02T17:00:00+09:00:00", end_datetime="2025-04-02T21:30:00+09:00:00", timezone="Asia/Tokyo"), Shift(summary="バイト", start_datetime="2025-04-04T17:00:00+09:00:00", end_datetime="2025-04-04T21:00:00+09:00:00", timezone="Asia/Tokyo")]
            >>> dummy_shifts_dict = [
            ...     {"summary":"バイト", "start_datetime":"2025-04-02T17:00:00+09:00:00", "end_datetime":"2025-04-02T21:30:00+09:00:00", "timezone":"Asia/Tokyo"},
            ...     {"summary":"バイト", "start_datetime":"2025-04-04T17:00:00+09:00:00", "end_datetime":"2025-04-04T21:00:00+09:00:00", "timezone":"Asia/Tokyo"}
            ... ]
            >>>
            >>> # --- 2. 外部依存をモック化してテストを実行 ---
            >>> # `os.getenv` をモック化して、__init__がエラーにならないようにする
            >>> with patch("os.getenv", return_value="dummy-token"), \\
            ...      patch("__main__.App") as MockApp, \\
            ...      patch("__main__.Shift.to_dict") as mock_to_dict:
            ...         # --- モックの設定 ---
            ...         # Appインスタンスが持つclientのchat_postMessageをモック化
            ...         mock_app_instance = MockApp.return_value    # self._app == mock_app_instanceとなるようにする
            ...         mock_post = mock_app_instance.client.chat_postMessage
            ...         mock_to_dict.side_effect = dummy_shifts_dict
            ...
            ...         # --- テスト対象の実行 ---
            ...         test_client = SlackClient(controller=mock_controller)
            ...         test_client.post_result(test_file, test_shifts)
            ...
            >>> # --- 3. 結果の検証 ---
            >>> assert mock_to_dict.call_count == 2
            >>>
            >>> # 1回だけ呼ばれたことを確認
            >>> mock_post.assert_called_once()
            >>>
            >>> # 意図した通りのメッセージが生成されたかを確認
            >>> expected_text = "シフト情報\\n- 2025-04-02 17:00 ~ 2025-04-02 21:30\\n- 2025-04-04 17:00 ~ 2025-04-04 21:00"
            >>>
            >>> # 正しい引数で呼ばれたかを確認
            >>> mock_post.assert_called_with(channel="C222", thread_ts="1648825135.123", text=expected_text)
        """
        channel = file.channel_id
        timestamp = file.timestamp
        result_text = (
            "以下のシフトをGoogleカレンダーに予定として追加しました。"
        )
        for shift in shifts:
            shift_dict = shift.to_dict()
            tmp = (
                "\n・ "
                + shift_dict["start_datetime"][:10]
                + " "
                + shift_dict["start_datetime"][11:16]
                + " ~ "
                + shift_dict["end_datetime"][:10]
                + " "
                + shift_dict["end_datetime"][11:16]
            )
            result_text += tmp

        self._app.client.chat_postMessage(
            channel=channel, thread_ts=timestamp, text=result_text
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
