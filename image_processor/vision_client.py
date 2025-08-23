"""Vision APIとアプリケーション間のやり取りを行うモジュール"""

from dotenv import load_dotenv

load_dotenv()
import os
from google.cloud import vision
import json
from google.oauth2 import service_account
import googleapiclient.discovery

from unittest.mock import MagicMock, patch


class VisionClient:
    """Vision APIを使って画像からデータを抽出するクラス
    Attributes:
        _api_key (str): Vision APIを利用するための鍵のパス
        _creds (:obj:`google.oauth2.service_account.Credentials`): 認証情報
        _client (:obj:`google.cloud.vision_v1.ImageAnnotatorClient`): Vision APIとのやりとりを担うオブジェクト
    """

    def __init__(self):
        self._api_key = os.getenv("GOOGlE_CLOUD_API_KEY_PATH")
        self._creds = service_account.Credentials.from_service_account_file(
            self._api_key
        )
        self._client = vision.ImageAnnotatorClient(credentials=self._creds)

    def extract_data_from_image(self, result_dir: str) -> None:
        """画像からデータを抽出するメソッド
        Args:
            result_dir (str):画像や抽出結果ファイルを格納するディレクトリへのパス
        Returns:
            None
        Examples:
            >>> # --- 1. テスト準備 ---
            >>> from unittest.mock import patch, MagicMock, mock_open
            >>>
            >>> # --- 2. ダミーやモックの設定 ---
            >>> test_result_dir = "result/dummy"
            >>> mock_image_content = b"dummy image data"
            >>> dummy_key_path = "dummy/key.json"
            >>> # MessageToDictが返す辞書データ
            >>> mock_response_dict = {"text_annotations": [{"description": "test"}]}
            >>>
            >>> # --- 3. 外部依存をモック化してテストを実行 ---
            >>> with patch('os.getenv', return_value=dummy_key_path), \\
            ...      patch("google.oauth2.service_account.Credentials.from_service_account_file") as mock_from_file, \\
            ...      patch("google.cloud.vision.ImageAnnotatorClient") as MockClient, \\
            ...      patch("google.cloud.vision.Image") as MockImage, \\
            ...      patch("google.cloud.vision.AnnotateImageResponse") as MockResponse, \\
            ...      patch("builtins.open", mock_open(read_data=mock_image_content)) as mock_file, \\
            ...      patch("json.dump") as mock_json_dump:
            ...     # --- モックのインスタンスと返り値を設定 ---
            ...     mock_api_response = MagicMock() # Vision APIからのレスポンスを模したMagicMockオブジェクト
            ...     mock_client_instance = MockClient.return_value  # self._client == mock_client_instanceとなるようにする
            ...     mock_client_instance.document_text_detection.return_value = mock_api_response
            ...     mock_image_instance = MockImage.return_value    # image == mock_image_instanceとなるようにする
            ...     MockResponse.to_dict.return_value = mock_response_dict
            ...
            ...     # --- 4. テスト対象の実行 ---
            ...     test_client = VisionClient()
            ...     test_client.extract_data_from_image(test_result_dir)
            ...
            >>> # --- 5. 結果の検証 ---
            >>> mock_from_file.assert_called_once_with(dummy_key_path)
            >>>
            >>> # 画像ファイルが正しく読み込まれたか
            >>> mock_file.assert_any_call(f"{test_result_dir}/shift.jpg", "rb")
            >>>
            >>> # vision.Imageオブジェクトが正しい内容で作成されたか
            >>> MockImage.assert_called_once_with(content=mock_image_content)
            >>>
            >>> # document_text_detectionが正しい引数で呼び出されたか
            >>> mock_client_instance.document_text_detection.assert_called_once_with(image=mock_image_instance)
            >>>
            >>> # APIレスポンスが辞書に変換されたか
            >>> MockResponse.to_dict.assert_called_once_with(mock_api_response)
            >>>
            >>> # JSONファイルが正しく書き込まれたか
            >>> mock_file.assert_any_call(f"{test_result_dir}/response.json", "w", encoding="utf-8")
            >>> write_handle = mock_file()
            >>> mock_json_dump.assert_called_with(mock_response_dict, write_handle, ensure_ascii=False, indent=2)
        """
        with open(f"{result_dir}/shift.jpg", "rb") as f:
            content = f.read()
        image = vision.Image(content=content)

        response = self._client.document_text_detection(image=image)

        # Vision APIからのレスポンスを辞書型に変換
        response_dict = vision.AnnotateImageResponse.to_dict(response)
        with open(f"{result_dir}/response.json", "w", encoding="utf-8") as f:
            json.dump(response_dict, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
