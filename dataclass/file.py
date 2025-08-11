"""Slack上のファイル情報を管理するモジュール
"""

import dataclasses
import datetime


@dataclasses.dataclass
class File:
    """Slack上のファイル情報を記録するデータクラス
    Attributes:
        id (str): Slackワークスペース内で各ファイルに一意に割り当てられるID
        name (str): Slackにアップロードされた時のファイル名
        private_url (str): Slack上のファイルをダウンロードするためのURL
        channel_id (str): やり取りが行われているチャンネル
        timestamp (datetime): ファイルが共有されたメッセージのタイムスタンプ
    """
    id: str
    name: str
    private_url: str
    channel_id: str
    timestamp: datetime