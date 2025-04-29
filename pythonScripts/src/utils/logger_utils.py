from datetime import datetime
import logging
import os

def setup_logger():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "..","..", "logs")
    os.makedirs(LOG_DIR, exist_ok=True)
    LOG_FILE = os.path.join(LOG_DIR, f"validationLog_{timestamp}.log")
    
    logger = logging.getLogger("validation_logger")
    logger.setLevel(logging.DEBUG)  # Set the root logger to DEBUG level

    if not logger.handlers:
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setLevel(logging.DEBUG)  # Set file handler to DEBUG level

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
    return logger
