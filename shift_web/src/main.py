import os
from datetime import datetime
import shutil
import logging

from src.utils import set_logging
from src.controller import Controller


def main(image_file_path: str) -> None:
    # 結果出力用ファイルの作成
    now_str = datetime.now().strftime("%Y%m%d%H%M%S")
    result_dir = f"src/result/{now_str}"
    os.makedirs(result_dir)

    # ログ設定
    logger = logging.getLogger(__name__)
    set_logging(result_dir)

    # Django上でアップロードされた画像をresult_dirにコピー
    shutil.copy(image_file_path, f"{result_dir}/shift.jpg")

    controller = Controller(result_dir=result_dir)
    controller.run()


if __name__ == "__main__":
    main()
