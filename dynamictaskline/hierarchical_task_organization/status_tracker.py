# StatusTracker class to keep track of task status.
class StatusTracker:
    def __init__(self):
        self.status = {}

    def update_status(self, task_name, status):
        self.status[task_name] = status
