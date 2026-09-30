from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    app_name: str = "ComicCraft"

    gemini_api_key: str = ""

    gemini_flash_model: str = "gemini-2.5-flash"

    gemini_pro_model: str = "gemini-2.5-pro"

    mock_image_generation: bool = True

    secret_key: str = "change-me"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


@lru_cache
def get_settings():
    return Settings()