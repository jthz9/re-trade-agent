from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "RE-OptAgent"
    DATABASE_URL: str = "sqlite:///../data/re_opt_agent.db"
    # Add other environment variables here

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
