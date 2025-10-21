from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Optional

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding='utf-8',
        extra="ignore"
    )

    APP_NAME: str = "tarotoo-2api"
    APP_VERSION: str = "1.0.0"
    DESCRIPTION: str = "一个将 tarotoo.com 匿名聊天功能转换为兼容 OpenAI 格式 API 的高性能代理，内置 Cloudflare 穿透和伪流式生成功能。"

    API_MASTER_KEY: Optional[str] = "tarotoo-2api-default-key"
    
    API_REQUEST_TIMEOUT: int = 180
    NGINX_PORT: int = 8087
    PSEUDO_STREAM_DELAY: float = 0.01 # 伪流式输出的字符间隔（秒）

    DEFAULT_MODEL: str = "tarotoo-psychic-chat"
    KNOWN_MODELS: List[str] = ["tarotoo-psychic-chat"]

settings = Settings()
