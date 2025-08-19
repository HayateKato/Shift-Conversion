"""画像から抽出されたデータをシフトデータに変換するモジュール"""

import json
import re
from datetime import datetime

from dataclass.shift import Shift

from unittest.mock import MagicMock, patch


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
            [Shift(summary="バイト", start_datetime="2025-08-01T17:00:00+09:00:00", end_datetime="2025-08-01T21:30:00+09:00:00", timezone="Asia/Tokyo")]
        """
        with open("response.json") as f:
            response = json.load(f)

        # response.jsonの中身から処理に必要な部分のみを取り出す
        full_text_annotation = response["full_text_annotation"]
        page = full_text_annotation["pages"][0]
        context = list()
        for block in page["blocks"]:
            for paragraph in block["paragraphs"]:
                for word in paragraph["words"]:
                    for symbol in word["symbols"]:
                        text = symbol["text"]
                        vertices = symbol["bounding_box"]["vertices"]
                        context.append({"text": text, "vertices": vertices})

        # "coordinate": (x座標の平均値，y座標の平均値)とする
        processed_context = list()
        for d in context:
            processed_context.append(
                {
                    "text": d["text"],
                    "coordinate": (
                        (
                            d["vertices"][0]["x"]
                            + d["vertices"][1]["x"]
                            + d["vertices"][2]["x"]
                            + d["vertices"][3]["x"]
                        )
                        / 4,
                        (
                            d["vertices"][0]["y"]
                            + d["vertices"][1]["y"]
                            + d["vertices"][2]["y"]
                            + d["vertices"][3]["y"]
                        )
                        / 4,
                    ),
                }
            )

        # y座標の平均値で昇順にソート
        sorted_processed_context = sorted(
            processed_context, key=lambda x: x["coordinate"][1]
        )

        # y座標の平均値が近いものでグループ化
        line_context = list()
        current_line = [sorted_processed_context[0]]
        current_y = sorted_processed_context[0]["coordinate"][1]
        for d in sorted_processed_context[1:]:
            if abs(d["coordinate"][1] - current_y) < 10:
                current_line.append(d)
            else:
                line_context.append(current_line)
                current_line = [d]
            current_y = d["coordinate"][1]

        # グループ化した行ごとにx座標の平均値で並べ替え
        sorted_line_context = list()
        for line in line_context:
            sorted_line = sorted(line, key=lambda x: x["coordinate"][0])
            sorted_line_context.append(sorted_line)

        # シフトが入っていない行(00時00分以外)を除外
        removed_context = list()
        for sl in sorted_line_context:
            text = ""
            for t in sl:
                text += t["text"]
            if len(text) >= 16:
                removed_context.append(text)

        # 誤字(Iや|)を除外
        cleaned_context = list()
        for rc in removed_context:
            cleaned_rc = re.sub(r"[I|]", "", t)
            cleaned_context.append(cleaned_rc)

        # current_patternに一致する文字列をreplace_patternの形式に変換
        current_pattern = r"(\d{1,2}/\d{1,2}).(\d{2,3})時(\d{2})分(\d{1,2})時(\d{2})分"
        replace_pattern = r"\1,\2:\3,\4:\5"
        result_context = list()
        for cc in cleaned_context:
            text = re.sub(current_pattern, replace_pattern, cc)
            splited_text = text.split(",")
            result_line = list()
            for st in splited_text:
                result_line.append(st)
            result_context.append(result_line)

        # シフトデータの作成
        summary = "バイト"  # summaryは固定
        year = datetime.now().year  # 年は現在のもの
        time_difference = "+09:00:00"  # 時差は+9時間
        timezone = "Asia/Tokyo"  # タイムゾーンは東京(Asia/Tokyo)
        shifts = list()
        for rc in result_context:
            date = rc[0].split("/")  # 月と日に分ける
            start_time = rc[1].split(":")  # 時と分に分ける
            end_time = rc[2].split(":")

            # yyyy-mm-ddThh:mm:ss+hh:mm:ssの形式にする
            start_datetime = datetime(
                year=year,
                month=int(date[0]),
                day=int(date[1]),
                hour=int(start_time[0]),
                minute=int(start_time[1]),
            )
            splited_start_datetime = str(start_datetime).split(" ")
            start_datetime_str = (
                splited_start_datetime[0]
                + "T"
                + splited_start_datetime[1]
                + time_difference
            )

            end_datetime = datetime(
                year=year,
                month=int(date[0]),
                day=int(date[1]),
                hour=int(end_time[0]),
                minute=int(end_time[1]),
            )
            splited_end_datetime = str(end_datetime).split(" ")
            end_datetime_str = (
                splited_end_datetime[0]
                + "T"
                + splited_end_datetime[1]
                + time_difference
            )

            shift = Shift(
                summary=summary,
                start_datetime=start_datetime_str,
                end_datetime=end_datetime_str,
                timezone=timezone,
            )
            shifts.append(shift)

        return shifts


if __name__ == "__main__":
    import doctest

    doctest.testmod()
