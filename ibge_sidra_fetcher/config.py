import configparser
import logging.config
import os
from pathlib import Path

CONFIG_DIR = os.getenv("CONFIG_DIR")
if not CONFIG_DIR:
    raise FileNotFoundError("No configuration directory found in environment variables")
CONFIG_DIR = Path(CONFIG_DIR)
DATA_DIR = os.getenv("DATA_DIR")
if not DATA_DIR:
    raise FileNotFoundError("No data directory found in environment variables")
DATA_DIR = Path(DATA_DIR) / "raw" / "ibge" / "sidra"

_config = configparser.ConfigParser()
_config.read(CONFIG_DIR / "ibge-sidra-fetcher" / "config.ini")

USER_AGENT = _config["DEFAULT"]["USER_AGENT"]
HTTP_HEADERS = {
    "User-Agent": USER_AGENT,
}
TIMEOUT = int(_config["DEFAULT"]["TIMEOUT"])

_logging_config_filepath = CONFIG_DIR / "ibge-sidra-fetcher" / "logging.ini"
if not _logging_config_filepath.exists():
    raise FileNotFoundError("No logging configuration file exists")
logging.config.fileConfig(_logging_config_filepath)
