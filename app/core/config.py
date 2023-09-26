import pytz

from pydantic_settings import BaseSettings
from starlette.config import Config

config = Config(".env")


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True

    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    JWT_SCRECT_KEY: str = "fastapi"
    JWT_REFRESH_SECRET_KEY: str = "fastapi"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # 30분
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 1주일

    # Postgres
    POSTGRES_HOST: str = "127.0.0.1"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "postgres"

    # # misc
    TIMEZONE = pytz.timezone("Asia/Seoul")


class DevelopmentConfig(Config):
    pass


class LocalConfig(Config):
    pass


class ProductionConfig(Config):
    DEBUG: str = False


def get_config():
    env = config("ENV")
    config_type = {
        "dev": DevelopmentConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
