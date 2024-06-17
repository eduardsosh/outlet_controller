"""
Module to provide logging capabilities
"""

import logging

class Logger:
    def __init__(self, log_file='app.log', level=logging.INFO):
        # Configure logging
        logging.basicConfig(
            level=level,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename=log_file,
            filemode='w'  # Set to 'a' for append mode
        )
        self.logger = logging.getLogger(__name__)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

