import logging.config
import os
from pathlib import Path

from pydantic_settings import BaseSettings

os.chdir(Path(__file__).parent.parent.parent)


class Configuration(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 5000
    DEBUG: bool = True
    LOGGING_PATH: str = "/config/logging.ini"
    DB_PATH: str = "/config/db.ini"
    DB_PASS_PATH: str = "/run/secrets/db_password"


class LocalConfiguration(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 5000
    DEBUG: bool = True
    LOGGING_PATH: str = "./config/logging.ini"
    DB_PATH: str = "./config/db_local.ini"
    DB_PASS_PATH: str = "./db_password.txt"
    # LOGGING_PATH: str = "../../config/logging.ini"
    # DB_PATH: str = "../../config/db_local.ini"
    # DB_PASS_PATH: str = "../../db_password.txt"


print("Current working directory", os.getcwd())
config = LocalConfiguration()

logging.config.fileConfig(config.LOGGING_PATH, disable_existing_loggers=False)
log = logging.getLogger(__name__)
