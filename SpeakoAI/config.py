
import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    AI_API: str = os.getenv("AI_API")
    VOICE2TEXT: str = os.getenv("VOICE2TEXT")

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")


    API_BASE_URL: str = os.getenv("API_BASE_URL")

    @property
    def async_db_url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"



settings = Settings()
