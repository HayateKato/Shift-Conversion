"""Vision APIとアプリケーション間のやり取りを行うモジュール
"""

from google.cloud import vision
from unittest.mock import MagicMock, patch


class VisionAPIClient:
    """Vision APIを使って画像からデータを抽出するクラス
    Attributes:
        _api_key (str): Vision APIを利用するための鍵のパス
        _client (:obj:`google.cloud.vision_v1.ImageAnnotatorClient`)
    """
    def __init__(self):
        pass

    def extract_data_from_image(self, result_dir: str) -> None:
        """画像からデータを抽出するメソッド
        Args:
            result_dir (str):画像や抽出結果ファイルを格納するディレクトリへのパス
        Returns:
            None
        Examples:
            >>> from google.cloud import vision
            >>> from unittest.mock import patch, MagicMock, mock_open
            >>> test_result_dir = "../result/dummy"
            >>> mock_response = MagicMock()
            >>> mock_response_dict = {"fullTextAnnotation": {"text": "抽出されたテキスト"}}
            >>> with patch("vision.ImageAnnotatorClient") as MockClient:
            ...     with patch("vision.Image") as MockImage:
            ...         with patch.object("builtins.open", mock_open()) as mock_file:
            ...             with patch("json.dump") as mock_json_dump:
            ...                 test_client = VisionAPIClient()
            ...                 AnnotateImageResponse.to_dict = MagicMock(return_value=mock_response_dict)
            ...                 test_client.extract_data_from_image(test_result_dir)
            >>> mock_file.assert_any_call(f"{test_result_dir}/test.jpg", "rb")
            >>> mock_client_instance.document_text_detection.assert_called_once_with(test_result_dir)
            >>> mock_file.assert_any_call(f"{test_result_dir}/test_response.json", "w", encoding="utf-8")
            >>> file_handle = mock_file()
            >>> mock_json_dump.assert_called_once_with(mock_response_dict, file_handle, ensure_ascii=False, indent=2)
            >>> file_handle.write.assert_any_call(mock_response_dict)
            >>> print("Test passed")
            Test passed
        """
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()