"""Config import function"""
import os

from dotenv import load_dotenv


def _getenv(key, default=None) -> str:
    value = os.environ.get(key, default)
    if value is None:
        raise NameError(f'Environment key "{key}" not found, recheck your .env file.')
    return value


load_dotenv()


class Config:
    """Service configurations"""

    # app setting
    APP_TITLE = _getenv("APP_TITLE", "FastAPI template")
    APP_DESCRIPTION = _getenv("APP_DESCRIPTION", "A template for FastAPI.")
    VERSION = _getenv("VERSION", "87")
    OPENAPI_URL = _getenv("OPENAPI_URL", "/openapi.json")

    # Redis setting
    REDIS_URL = _getenv("REDIS_URL", "redis://:password@redis:6379/0")

    # PostgreSQL setting
    PG_HOST = _getenv("PG_HOST", "postgres")
    PG_PORT = _getenv("PG_PORT", 5432)
    PG_DATABASE = _getenv("PG_DATABASE", "m3ow87")
    PG_USERNAME = _getenv("PG_USERNAME", "m3ow87")
    PG_PASSWORD = _getenv("PG_PASSWORD", "m3ow87")
