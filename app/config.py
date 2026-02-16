from pydantic_settings import BaseSettings
from pydantic import field_validator
from typing import Union


class Settings(BaseSettings):
  app_name: str = "FastAPI Shop"
  debug: bool = True
  
  # PostgreSQL
  postgres_user: str = "shop_user"
  postgres_password: str = "shop_password"
  postgres_db: str = "shop_db"
  postgres_host: str = "localhost"
  postgres_port: int = 5432
  
  cors_origins: Union[str, list[str]] = "http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173,http://127.0.0.1:3000"
  static_dir: str = "static"
  images_dir: str = "static/images"

  @field_validator('cors_origins', mode='before')
  @classmethod
  def parse_cors_origins(cls, v):
    if isinstance(v, str):
      return [origin.strip() for origin in v.split(',')]
    return v

  @property
  def database_url(self) -> str:
    return (
      f"postgresql://{self.postgres_user}:{self.postgres_password}"
      f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
    )

  class Config:
    env_file = '.env'


settings = Settings()
