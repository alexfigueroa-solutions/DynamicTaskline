from .task import Task

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, title):
        self.tasks[title] = Task(title)

    def add_subtask(self, task_title, subtask_title):
        if task_title in self.tasks:
            self.tasks[task_title].add_subtask(subtask_title)

    def run_all(self):
        for task in self.tasks.values():
            task.run()
