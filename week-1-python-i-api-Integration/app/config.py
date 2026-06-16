from functools import lru_cache
from typing import Literal
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


ProviderName = Literal["echo", "ollama", "openai_compatible"]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "Week 1 Async AI Chat API"
    provider: ProviderName = Field(default="echo", alias="AI_PROVIDER")
    max_history_messages: int = Field(default=12, alias="MAX_HISTORY_MESSAGES")

    ollama_base_url: str = Field(default="http://localhost:11434", alias="OLLAMA_BASE_URL")
    ollama_model: str = Field(default="gemma2:2b", alias="OLLAMA_MODEL")

    openai_compatible_base_url: str = Field(
        default="https://api.openai.com/v1",
        alias="OPENAI_COMPATIBLE_BASE_URL",
    )
    openai_compatible_api_key: str | None = Field(
        default=None,
        alias="OPENAI_COMPATIBLE_API_KEY",
    )
    openai_compatible_model: str = Field(
        default="gpt-4o-mini",
        alias="OPENAI_COMPATIBLE_MODEL",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
