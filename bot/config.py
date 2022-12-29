"""
Модуль конфига бота.
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    SAVE_PATH: str


base_config = Settings(_env_file='.env')
