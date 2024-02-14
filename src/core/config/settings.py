import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class EnvSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )


class PostgresSettings(EnvSettings):
    db_user: str = Field(default="app")
    db_password: str = Field(default="123qwe")
    db_host: str = Field(default="localhost")
    db_port: int = Field(default=5432)
    db_name: str = Field(default="auth_db")


class RedisSettings(EnvSettings):
    redis_host: str = Field(default="127.0.0.1")
    redis_port: int = Field(default=6379)
    cache_expire_in_seconds: int = Field(default=(60 * 5))


class Settings(BaseSettings):
    pg: PostgresSettings = PostgresSettings()
    redis: RedisSettings = RedisSettings()


settings = Settings()
