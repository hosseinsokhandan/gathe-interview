from typing import Any, Dict, Optional
from pydantic import BaseSettings, PostgresDsn, validator, Field


class Settings(BaseSettings):
    DB_HOST: str = Field(default="127.0.0.1")
    DB_PORT: str = Field(default="5432")
    DB_NAME: str = Field(default="foo")
    DB_USER: str = Field(default="auth")
    DB_PASSWD: str = Field(default="123456")

    DATABASE_URI: Optional[PostgresDsn] = None

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("DB_USER"),
            password=values.get("DB_PASSWD"),
            host=values.get("DB_HOST"),
            port=values.get("DB_PORT"),
            path=f"/{values.get('DB_NAME')}",
        )

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
