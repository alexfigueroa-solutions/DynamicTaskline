# TaskManager.py
from .task import Task

# TaskManager class to manage the execution of tasks.
class TaskManager:
    def __init__(self):
        self.root_task = Task("Root")

    def add_task(self, task, parent=None):
        if parent is None:
            self.root_task.add_child(task)
        else:
            parent.add_child(task)

    def run(self):
        self.root_task.run()
        print("\nAll tasks executed.")
