from typing import Any, Dict, List, Optional
from functools import lru_cache
from pydantic import BaseSettings, PostgresDsn, validator, Field


class Settings(BaseSettings):
    DB_HOST: str = Field(default="127.0.0.1")
    DB_PORT: str = Field(default="5432")
    DB_NAME: str = Field(default="permission_system")
    DB_USER: str = Field(default="auth")
    DB_PASSWD: str = Field(default="123456")

    MODELS: List = [
        "models.document",
        "models.member",
        "models.permission",
        "aerich.models",  # aerich
    ]

    DATABASE_URL: Optional[PostgresDsn] = None

    @validator("DATABASE_URL", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgres",
            user=values.get("DB_USER"),
            password=values.get("DB_PASSWD"),
            host=values.get("DB_HOST"),
            port=values.get("DB_PORT"),
            path=f"/{values.get('DB_NAME')}",
        )

    class Config:
        case_sensitive: bool = True
        env_file: str = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
