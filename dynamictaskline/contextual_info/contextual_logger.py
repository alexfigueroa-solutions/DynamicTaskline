from .info_logger import InfoLogger

# ContextualLogger class to provide context-aware logging.
class ContextualLogger(InfoLogger):
    def __init__(self, name, context_manager):
        super().__init__(name)
        self.context_manager = context_manager
