import logging

# InfoLogger class that uses Python's built-in logging framework.
class InfoLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def log(self, message):
        self.logger.info(message)
