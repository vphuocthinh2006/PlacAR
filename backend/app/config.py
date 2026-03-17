from functools import lru_cache
from pydantic import BaseModel
import os


class Settings(BaseModel):
    app_name: str = "DecoAR / RoomFit Backend"
    environment: str = os.getenv("ENV", "development")
    llm_api_key: str | None = os.getenv("LLM_API_KEY")
    llm_provider: str | None = os.getenv("LLM_PROVIDER")  # "openai", "gemini", ...


@lru_cache
def get_settings() -> Settings:
    return Settings()

