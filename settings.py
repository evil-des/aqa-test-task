from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BASE_URL: str = "https://effective-mobile.ru"


settings = Settings()
