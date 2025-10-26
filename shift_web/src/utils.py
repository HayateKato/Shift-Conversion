"""便利な関数群"""

import logging


def set_logging(result_dir: str) -> "logging.Logger":
    """
    ログをファイルに書き出すよう設定する関数．
    Args:
        result_dir (str): ログの出力先
    Returns:
        設定済みのrootのlogger

    Example:
    >>> logger = logging.getLogger(__name__)
    >>> set_logging(result_dir)
    >>> logger.info('log message...')
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # ログレベル
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    # ログのフォーマット

    # ファイル出力へのログ出力設定
    file_handler = logging.FileHandler(f"{result_dir}/log.log", "w")
    # ログ出力ファイル
    file_handler.setLevel(logging.DEBUG)  # 出力ログレベル
    file_handler.setFormatter(formatter)  # フォーマットを指定
    logger.addHandler(file_handler)
    return logger
