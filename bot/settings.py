from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    TOKEN: SecretStr
    CHAT_ID: int

    class Config:
        env_file = ".env", "stack.env"
        env_file_encoding = "utf-8"


settings = Settings()
