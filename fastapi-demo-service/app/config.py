from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables
    """

settings = Settings()