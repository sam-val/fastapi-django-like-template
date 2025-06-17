import os
from typing import List, Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings pulled from environment variables or a .env file.
    You can extend this with your own config (e.g. SMTP, 3rd party APIs, etc.).
    """

    app_name: str = "fastapi-django-like-template"
    debug: bool = False
    allowed_origins: List[str] = Field(default_factory=list)

    # database
    database_url: str
    redis_url: Optional[str] = None

    # Add more custom settings as needed
    # e.g. rate_limit_per_minute: int = 30

    model_config = SettingsConfigDict(
        # `.env.prod` takes priority over `.env`
        env_file=(".env", ".env.prod"),
        env_file_encoding="utf-8",
        extra="allow",
    )


def load_settings_from_vault() -> Settings:
    """
    Placeholder for loading secrets from a secret manager like HashiCorp Vault.
    Replace with your logic if you decide to move away from .env files.
    """
    raise NotImplementedError("Vault integration is not implemented.")


def get_settings() -> Settings:
    """
    Returns application settings. Chooses between environment file and Vault.
    Set `USE_VAULT=true` in your environment to switch to vault loader.
    """
    if os.getenv("USE_VAULT", "false").lower() == "true":
        return load_settings_from_vault()
    return Settings()


settings = get_settings()
