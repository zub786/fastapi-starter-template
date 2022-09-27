from pydantic import BaseSettings


class Settings(BaseSettings):
    env: str = "develop"


settings = Settings()
