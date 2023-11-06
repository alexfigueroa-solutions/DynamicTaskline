# ErrorHandler class to handle exceptions.
class ErrorHandler:
    @staticmethod
    def handle_error(error, logger):
        logger.error(str(error))
