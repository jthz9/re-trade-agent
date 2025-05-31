from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "RE-OptAgent"
    # Add other environment variables here

    class Config:
        env_file = ".env"


settings = Settings()
