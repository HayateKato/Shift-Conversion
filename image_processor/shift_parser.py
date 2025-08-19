"""画像から抽出されたデータをシフトデータに変換するモジュール
"""

from dataclass.shift import Shift


class ShiftParser:
    """画像から抽出されたデータをシフトデータに変換するモジュール
    Attributes:
        None
    """
    def __init__(self):
        pass

    def parse_data_to_shifts(self, result_dir: str) -> list[Shift]:
        """画像から抽出されたデータを使ってシフトデータを作成するメソッド
        Args:
            result_dir (str):画像や抽出結果ファイルを格納するディレクトリへのパス
        Returns:
            list[Shift]: シフトデータ
        Examples:
            >>> from unittest.mock import patch, MagicMock, mock_open
            >>> from dataclass.shift import Shift
            >>> import json
            >>>
            >>> # ダミーを作成
            >>> test_result_dir = "result/dummy"
            >>> mock_json = {
            >>>     "text_annotations": [
            >>>         {
            >>>             "locale": "zh",
            >>>             "description": "8/1\n金\n17時00分\n21時30分",
            >>>             "bounding_poly": {
            >>>                 "vertices": [
            >>>                     {
            >>>                         "x": 32,
            >>>                         "y": 23
            >>>                     },
            >>>                     {
            >>>                         "x": 749,
            >>>                         "y": 23
            >>>                     },
            >>>                     {
            >>>                         "x": 749,
            >>>                         "y": 2058
            >>>                     },
            >>>                     {
            >>>                         "x": 32,
            >>>                         "y": 2058
            >>>                     }
            >>>                 ],
            >>>                 "normalized_vertices": []
            >>>             },
            >>>             "mid": "",
            >>>             "score": 0.0,
            >>>             "confidence": 0.0,
            >>>             "topicality": 0.0,
            >>>             "locations": [],
            >>>             "properties": []
            >>>         },
            >>>         {
            >>>             "description": "8/1",
            >>>             "bounding_poly": {
            >>>                 "vertices": [
            >>>                     {
            >>>                         "x": 35,
            >>>                         "y": 23
            >>>                     },
            >>>                     {
            >>>                         "x": 82,
            >>>                         "y": 23
            >>>                     },
            >>>                     {
            >>>                         "x": 82,
            >>>                         "y": 49
            >>>                     },
            >>>                     {
            >>>                         "x": 35,
            >>>                         "y": 49
            >>>                     }
            >>>                 ],
            >>>                 "normalized_vertices": []
            >>>             },
            >>>             "mid": "",
            >>>             "locale": "",
            >>>             "score": 0.0,
            >>>             "confidence": 0.0,
            >>>             "topicality": 0.0,
            >>>             "locations": [],
            >>>             "properties": []
            >>>         },
            >>>         {
            >>>             "description": "金",
            >>>             "bounding_poly": {
            >>>                 "vertices": [
            >>>                     {
            >>>                         "x": 216,
            >>>                         "y": 23
            >>>                     },
            >>>                     {
            >>>                         "x": 247,
            >>>                         "y": 23
            >>>                     },
            >>>                     {
            >>>                         "x": 247,
            >>>                         "y": 49
            >>>                     },
            >>>                     {
            >>>                         "x": 216,
            >>>                         "y": 49
            >>>                     }
            >>>                 ],
            >>>                 "normalized_vertices": []
            >>>             },
            >>>             "mid": "",
            >>>             "locale": "",
            >>>             "score": 0.0,
            >>>             "confidence": 0.0,
            >>>             "topicality": 0.0,
            >>>             "locations": [],
            >>>             "properties": []
            >>>         },
            >>>         {
            >>>             "description": "17",
            >>>             "bounding_poly": {
            >>>                 "vertices": [
            >>>                     {
            >>>                         "x": 453,
            >>>                         "y": 26
            >>>                     },
            >>>                     {
            >>>                         "x": 485,
            >>>                         "y": 26
            >>>                     },
            >>>                     {
            >>>                         "x": 485,
            >>>                         "y": 52
            >>>                     },
            >>>                     {
            >>>                         "x": 453,
            >>>                         "y": 52
            >>>                     }
            >>>                 ],
            >>>                 "normalized_vertices": []
            >>>             },
            >>>             "mid": "",
            >>>             "locale": "",
            >>>             "score": 0.0,
            >>>             "confidence": 0.0,
            >>>             "topicality": 0.0,
            >>>             "locations": [],
            >>>             "properties": []
            >>>         },
            >>>         {
            >>>             "description": "時",
            >>>             "bounding_poly": {
            >>>                 "vertices": [
            >>>                     {
            >>>                         "x": 485,
            >>>                         "y": 26
            >>>                     },
            >>>                     {
            >>>                         "x": 512,
            >>>                         "y": 26
            >>>                     },
            >>>                     {
            >>>                         "x": 512,
            >>>                         "y": 52
            >>>                     },
            >>>                     {
            >>>                         "x": 485,
            >>>                         "y": 52
            >>>                     }
            >>>                 ],
            >>>                 "normalized_vertices": []
            >>>             },
            >>>             "mid": "",
            >>>             "locale": "",
            >>>             "score": 0.0,
            >>>             "confidence": 0.0,
            >>>             "topicality": 0.0,
            >>>             "locations": [],
            >>>             "properties": []
            >>>         },
            >>>         {
            >>>             "description": "00",
            >>>             "bounding_poly": {
            >>>                 "vertices": [
            >>>                     {
            >>>                         "x": 516,
            >>>                         "y": 26
            >>>                     },
            >>>                     {
            >>>                         "x": 549,
            >>>                         "y": 26
            >>>                     },
            >>>                     {
            >>>                         "x": 549,
            >>>                         "y": 52
            >>>                     },
            >>>                     {
            >>>                         "x": 516,
            >>>                         "y": 52
            >>>                     }
            >>>                 ],
            >>>                 "normalized_vertices": []
            >>>             },
            >>>             "mid": "",
            >>>             "locale": "",
            >>>             "score": 0.0,
            >>>             "confidence": 0.0,
            >>>             "topicality": 0.0,
            >>>             "locations": [],
            >>>             "properties": []
            >>>         },
            >>>         {
            >>>             "description": "分",
            >>>             "bounding_poly": {
            >>>                 "vertices": [
            >>>                     {
            >>>                         "x": 552,
            >>>                         "y": 26
            >>>                     },
            >>>                     {
            >>>                         "x": 580,
            >>>                         "y": 26
            >>>                     },
            >>>                     {
            >>>                         "x": 580,
            >>>                         "y": 52
            >>>                     },
            >>>                     {
            >>>                         "x": 552,
            >>>                         "y": 52
            >>>                     }
            >>>                 ],
            >>>                 "normalized_vertices": []
            >>>             },
            >>>             "mid": "",
            >>>             "locale": "",
            >>>             "score": 0.0,
            >>>             "confidence": 0.0,
            >>>             "topicality": 0.0,
            >>>             "locations": [],
            >>>             "properties": []
            >>>         },
            >>>         {
            >>>             "description": "21",
            >>>             "bounding_poly": {
            >>>                 "vertices": [
            >>>                     {
            >>>                         "x": 620,
            >>>                         "y": 26
            >>>                     },
            >>>                     {
            >>>                         "x": 652,
            >>>                         "y": 26
            >>>                     },
            >>>                     {
            >>>                         "x": 652,
            >>>                         "y": 52
            >>>                     },
            >>>                     {
            >>>                         "x": 620,
            >>>                         "y": 52
            >>>                     }
            >>>                 ],
            >>>                 "normalized_vertices": []
            >>>             },
            >>>             "mid": "",
            >>>             "locale": "",
            >>>             "score": 0.0,
            >>>             "confidence": 0.0,
            >>>             "topicality": 0.0,
            >>>             "locations": [],
            >>>             "properties": []
            >>>         },
            >>>         {
            >>>             "description": "時",
            >>>             "bounding_poly": {
            >>>                 "vertices": [
            >>>                     {
            >>>                         "x": 655,
            >>>                         "y": 26
            >>>                     },
            >>>                     {
            >>>                         "x": 681,
            >>>                         "y": 26
            >>>                     },
            >>>                     {
            >>>                         "x": 681,
            >>>                         "y": 51
            >>>                     },
            >>>                     {
            >>>                         "x": 655,
            >>>                         "y": 51
            >>>                     }
            >>>                 ],
            >>>                 "normalized_vertices": []
            >>>             },
            >>>             "mid": "",
            >>>             "locale": "",
            >>>             "score": 0.0,
            >>>             "confidence": 0.0,
            >>>             "topicality": 0.0,
            >>>             "locations": [],
            >>>             "properties": []
            >>>         },
            >>>         {
            >>>             "description": "30",
            >>>             "bounding_poly": {
            >>>                 "vertices": [
            >>>                     {
            >>>                         "x": 685,
            >>>                         "y": 26
            >>>                     },
            >>>                     {
            >>>                         "x": 718,
            >>>                         "y": 26
            >>>                     },
            >>>                     {
            >>>                         "x": 718,
            >>>                         "y": 51
            >>>                     },
            >>>                     {
            >>>                         "x": 685,
            >>>                         "y": 51
            >>>                     }
            >>>                 ],
            >>>                 "normalized_vertices": []
            >>>             },
            >>>             "mid": "",
            >>>             "locale": "",
            >>>             "score": 0.0,
            >>>             "confidence": 0.0,
            >>>             "topicality": 0.0,
            >>>             "locations": [],
            >>>             "properties": []
            >>>         },
            >>>         {
            >>>             "description": "分",
            >>>             "bounding_poly": {
            >>>                 "vertices": [
            >>>                     {
            >>>                         "x": 721,
            >>>                         "y": 26
            >>>                     },
            >>>                     {
            >>>                         "x": 749,
            >>>                         "y": 26
            >>>                     },
            >>>                     {
            >>>                         "x": 749,
            >>>                         "y": 51
            >>>                     },
            >>>                     {
            >>>                         "x": 721,
            >>>                         "y": 51
            >>>                     }
            >>>                 ],
            >>>                 "normalized_vertices": []
            >>>             },
            >>>             "mid": "",
            >>>             "locale": "",
            >>>             "score": 0.0,
            >>>             "confidence": 0.0,
            >>>             "topicality": 0.0,
            >>>             "locations": [],
            >>>             "properties": []
            >>>         },
            >>>     ],
            >>>     "full_text_annotation": {},
            >>>     "face_annotations": [],
            >>>     "landmark_annotations": [],
            >>>     "logo_annotations": [],
            >>>     "label_annotations": [],
            >>>     "localized_object_annotations": []
            >>> }
            >>> mock_json_str = json.dumps(mock_json)
            >>>
            >>> # 外部依存をモック化
            >>> with patch("builtins.open", mock_open(read_data=mock_json_str)) as mock_file:
            >>>     # テスト対象の実行
            ...     test_shift_parser = ShiftParser()
            ...     result_shift = test_shift_parser.parse_data_to_shifts(test_result_dir)
            ...
            >>> # jsonファイルが正しく読み込まれたか
            >>> mock_file.assert_any_call(f"{test_result_dir}/response.json", "r", encoding="utf-8)
            >>>
            >>> # 返り値が正しいか
            >>> result_shift
            [Shift(summary="バイト", start_datetime="2025-08-01T17:00:00+09:00", end_datetime="2025-08-01T21:30:00+09:00", timezone="Asia/Tokyo")]
        """
        pass