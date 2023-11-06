from .subtask import Subtask

class Task:
    def __init__(self, title):
        self.title = title
        self.subtasks = []
        self.status = "Not Started"

    def add_subtask(self, title):
        self.subtasks.append(Subtask(title))

    def run(self):
        self.status = "In Progress"
        # Simulating task execution
        print(f"Task '{self.title}' is {self.status}.")
        for subtask in self.subtasks:
            subtask.run()
        self.status = "Completed"
        print(f"Task '{self.title}' is {self.status}.")
