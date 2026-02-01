import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "logs"
LOG_FILE = "logs/trading_bot.log"

os.makedirs(LOG_DIR, exist_ok=True)

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    handler = RotatingFileHandler(
        LOG_FILE, maxBytes=5_000_000, backupCount=3
    )
    handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(console)
