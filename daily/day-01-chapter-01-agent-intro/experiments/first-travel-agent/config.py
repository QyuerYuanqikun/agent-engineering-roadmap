import os
from dataclasses import dataclass

from dotenv import load_dotenv


# 加载项目根目录下的 .env 文件
load_dotenv()


def get_required_env(name: str) -> str:
    """
    读取必需的环境变量。

    如果变量不存在或为空，立即抛出错误，
    避免程序带着错误配置继续运行。
    """
    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"缺少必需的环境变量: {name}"
        )

    return value


@dataclass(frozen=True)
class Settings:
    """
    项目的统一配置对象。
    """

    llm_api_key: str
    llm_base_url: str
    llm_model_id: str
    tavily_api_key: str


settings = Settings(
    llm_api_key=get_required_env("LLM_API_KEY"),
    llm_base_url=get_required_env("LLM_BASE_URL"),
    llm_model_id=get_required_env("LLM_MODEL_ID"),
    tavily_api_key=get_required_env("TAVILY_API_KEY"),
)
