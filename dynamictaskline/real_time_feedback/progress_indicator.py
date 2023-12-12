# real_time_feedback/progress_indicator.py

import time

class ProgressIndicator:
    def __init__(self, task_name):
        self.task_name = task_name

    def start(self):
        print(f"{self.task_name}: [", end="")

    def update(self, progress):
        print("#" * int(progress * 20), end="")

    def finish(self):
        print("] Done")
