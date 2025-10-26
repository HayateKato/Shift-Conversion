"""画像処理とシフトデータの作成を行うモジュール"""

from src.image_processor.vision_client import VisionClient
from src.image_processor.shift_parser import ShiftParser
from src.dataclass.shift import Shift

from unittest.mock import MagicMock, patch


class ImageProcessor:
    """画像処理とシフトデータの作成を行うクラス
    Attributes:
        _vision_client (:obj:`VisionClient`): Vision APIにおける処理を行うオブジェクト
        _shift_parser (:obj:`ShiftParser`): 画像から抽出されたデータをシフトデータに変換するオブジェクト
    """

    def __init__(self):
        self._vision_client = VisionClient()
        self._shift_parser = ShiftParser()

    def process_image(self, result_dir: str) -> list[Shift]:
        """画像処理とシフトデータの作成を行うメソッド
        Args:
            result_dir (str):画像や抽出結果ファイルを格納するディレクトリへのパス
        Returns:
            list[Shift]: シフトデータ
        Examples:
            >>> from unittest.mock import MagicMock, patch
            >>> from dataclass.shift import Shift
            >>>
            >>> test_result_dir = "result/dummy"
            >>> mock_shifts = [Shift(summary="バイト", start_datetime="2025-04-02T17:00:00+09:00:00", end_datetime="2025-04-02T21:30:00+09:00:00", timezone="Asia/Tokyo"), Shift(summary="バイト", start_datetime="2025-04-04T17:00:00+09:00:00", end_datetime="2025-04-04T21:00:00+09:00:00", timezone="Asia/Tokyo")]
            >>>
            >>> with patch("__main__.VisionClient") as MockClient, \\
            ...      patch("__main__.ShiftParser") as MockParser:
            ...     mock_client_instance = MockClient.return_value
            ...     mock_client_instance.extract_data_from_image.return_value = None
            ...     mock_parser_instance = MockParser.return_value
            ...     mock_parser_instance.parse_data_to_shifts.return_value = mock_shifts
            ...
            ...     # テスト対象を実行
            ...     test_image_processor = ImageProcessor()
            ...     result_shifts = test_image_processor.process_image(test_result_dir)
            ...
            >>> # 正しい引数で呼び出されたか
            >>> mock_client_instance.extract_data_from_image.assert_called_once_with(test_result_dir)
            >>> mock_parser_instance.parse_data_to_shifts.assert_called_once_with(test_result_dir)
            >>>
            >>> # 返り値が正しいか
            >>> result_shifts
            [Shift(summary='バイト', start_datetime='2025-04-02T17:00:00+09:00:00', end_datetime='2025-04-02T21:30:00+09:00:00', timezone='Asia/Tokyo'), Shift(summary='バイト', start_datetime='2025-04-04T17:00:00+09:00:00', end_datetime='2025-04-04T21:00:00+09:00:00', timezone='Asia/Tokyo')]
        """
        self._vision_client.extract_data_from_image(result_dir)
        shifts = self._shift_parser.parse_data_to_shifts(result_dir)

        return shifts


if __name__ == "__main__":
    import doctest

    doctest.testmod()
