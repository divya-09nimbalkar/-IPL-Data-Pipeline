from datetime import datetime
import logging
from pathlib import Path

log_file = Path(__file__).resolve().parent.parent / "logs" / "pipeline.log"
log_file.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

def log_message(msg: str, level: str = "info"):
    timestamped = f"[{datetime.now()}] {msg}"
    print(timestamped)

    if level == "info":
        logging.info(msg)
    elif level == "warning":
        logging.warning(msg)
    elif level == "error":
        logging.error(msg)
