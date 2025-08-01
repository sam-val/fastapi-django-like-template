import os
from enum import Enum
from functools import lru_cache
from typing import Any, List

import redis.asyncio as redis
from pydantic import Field, PostgresDsn, RedisDsn, field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModeEnum(str, Enum):
    testing = "testing"  # for pytest
    local = "local"
    dev = "dev"
    uat = "uat"
    prod = "prod"


class Settings(BaseSettings):
    """
    Application settings pulled from environment variables or a .env file.
    You can extend this with your own config (e.g. SMTP, 3rd party APIs, etc.).
    """

    APP_NAME: str = "fastapi-django-like-template"
    DEBUG: bool = False
    ALLOWED_ORIGINS: List[str] = Field(default_factory=list)
    MODE: ModeEnum = ModeEnum.dev

    # database
    ASYNC_SQLITE_URI: str = ""

    # assume postgres as default
    DATABASE_USER: str = ""
    DATABASE_PASSWORD: str = ""
    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 5432
    DATABASE_NAME: str = "postgres"

    # test db
    TEST_DATABASE_USER: str = ""
    TEST_DATABASE_PASSWORD: str = ""
    TEST_DATABASE_HOST: str = ""
    TEST_DATABASE_PORT: int = 5432
    TEST_DATABASE_NAME: str = ""

    DATABASE_URI: PostgresDsn | str = ""
    ASYNC_DATABASE_URI: PostgresDsn | str = ""

    # redis
    REDIS_URI: RedisDsn | str = ""
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PATH: str = "/0"

    # Add more custom settings as needed
    # e.g. rate_limit_per_minute: int = 30

    @field_validator("REDIS_URI", mode="after")
    def assemble_redis_uri(cls, v: str | None, info: ValidationInfo) -> Any:
        if isinstance(v, str):
            if v == "":
                return RedisDsn.build(
                    scheme="redis",
                    host=info.data.get("REDIS_HOST", "localhost"),
                    port=info.data.get("REDIS_PORT", 6379),
                    path=info.data.get("REDIS_PATH", "/0"),
                )
        return v

    @field_validator("DATABASE_URI", mode="after")
    def assemble_sync_db(cls, v: str | None, info: ValidationInfo) -> Any:
        if isinstance(v, str):
            if v == "":
                return PostgresDsn.build(
                    scheme="postgresql",
                    username=info.data["DATABASE_USER"],
                    password=info.data["DATABASE_PASSWORD"],
                    host=info.data["DATABASE_HOST"],
                    port=info.data["DATABASE_PORT"],
                    path=info.data["DATABASE_NAME"],
                )
        return v

    @field_validator("ASYNC_DATABASE_URI", mode="after")
    def assemble_async_db(cls, v: str | None, info: ValidationInfo) -> Any:
        if isinstance(v, str):
            if v == "":
                mode = info.data.get("MODE")
                if mode == ModeEnum.testing:
                    return PostgresDsn.build(
                        scheme="postgresql+asyncpg",
                        username=info.data["TEST_DATABASE_USER"],
                        password=info.data["TEST_DATABASE_PASSWORD"],
                        host=info.data["TEST_DATABASE_HOST"],
                        port=info.data["TEST_DATABASE_PORT"],
                        path=info.data["TEST_DATABASE_NAME"],
                    )

                return PostgresDsn.build(
                    scheme="postgresql+asyncpg",
                    username=info.data["DATABASE_USER"],
                    password=info.data["DATABASE_PASSWORD"],
                    host=info.data["DATABASE_HOST"],
                    port=info.data["DATABASE_PORT"],
                    path=info.data["DATABASE_NAME"],
                )
            return v

    @field_validator("ASYNC_SQLITE_URI", mode="after")
    def assemble_test_db(cls, v: str | None, info: ValidationInfo) -> Any:
        # we uses 2 testing db, one for dev one for unittest
        mode = info.data.get("MODE")
        if v == "":
            if mode == ModeEnum.testing:
                return "sqlite+aiosqlite:///./unittest.db"
            return "sqlite+aiosqlite:///./test.db"

        return v

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


# lru cache for singleton pattern
@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """
    Returns application settings. Chooses between environment file and Vault.
    Set `USE_VAULT=true` in your environment to switch to vault loader.
    """
    if os.getenv("USE_VAULT", "false").lower() == "true":
        return load_settings_from_vault()
    return Settings()
