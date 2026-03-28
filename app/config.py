from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    anthropic_api_key: str = ""
    secret_key: str = "change-me"
    data_dir: Path = Path("./data")
    database_path: Path = Path("./app.db")
    alert_email: str = ""
    default_spending_limit_cents: int = 1000  # $10.00
    jwt_algorithm: str = "HS256"
    jwt_expire_hours: int = 24

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
