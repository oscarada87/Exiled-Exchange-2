import logging
from parser import Parser

from services.logger_setup import logger, set_log_level

SUPPORTED_LANGUAGES = ["en", "ru", "ko", "cmn-Hant"]


if __name__ == "__main__":
    logger.info("Starting parser")
    set_log_level(logging.WARNING)
    for lang in SUPPORTED_LANGUAGES:
        logger.info(f"Generating {lang} tables")
        parser = Parser(lang)
        parser.run()
