# hierarchical_task_organization/leaf_task.py

from .task import Task

class LeafTask(Task):
    def __init__(self, name, action):
        super().__init__(name)
        self.action = action
        self.status = "Initialized"

    def execute(self):
        print(f"Executing '{self.name}'...")
        self.action()
        print(f"Completed '{self.name}'.")
