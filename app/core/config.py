from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Absolute path to project root
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
env_path = os.path.join(ROOT_DIR, ".env")

# Load .env file explicitly
if os.path.exists(env_path):
    load_dotenv(dotenv_path=env_path)
else:
    raise FileNotFoundError(f".env file not found at {env_path}")

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    MODEL_NAME: str
    EMBEDDING_MODEL: str
    VECTOR_DIM: int = 3072
    TOP_K: int = 5

    class Config:
        env_file = env_path

# Create the settings instance
settings = Settings()

# Debug: print values to make sure .env loaded
print("OPENAI_API_KEY:", settings.OPENAI_API_KEY)
print("MODEL_NAME:", settings.MODEL_NAME)
print("EMBEDDING_MODEL:", settings.EMBEDDING_MODEL)
