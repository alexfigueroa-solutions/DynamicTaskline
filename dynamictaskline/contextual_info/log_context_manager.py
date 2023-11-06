from .log_context import LogContext

# LogContextManager class to manage multiple LogContexts.
class LogContextManager:
    def __init__(self):
        self.contexts = {}

    def create_context(self, task_name):
        self.contexts[task_name] = LogContext(task_name)

    def get_context(self, task_name):
        return self.contexts.get(task_name)
