from pathlib import Path

from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    users: str = "/users"
    profile: str = "/profile"
    country: str = "/country"
    auth: str = "/auth"
    social_link: str = "/social_link"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class AuthJWT(BaseModel):
    private_key_path: Path = None
    public_key_path: Path = None
    algorithm: str = None
    access_token_expire_minutes: int = 3
    refresh_token_expire_days: int = 30
    # refresh_token_expire_minutes: int = 60 * 24 * 30

class LogConfig(BaseModel):
    log_path: Path = "log_core/logs_json/info.log"
    format: str = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
    level: str = "DEBUG"
    rotation: str = "00:00"
    retention: str = "1 days"
    compression: str = "zip"
    serialize: bool = False



class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    loger: LogConfig = LogConfig()
    auth_jwt: AuthJWT = AuthJWT()
    db: DatabaseConfig



settings = Settings()
