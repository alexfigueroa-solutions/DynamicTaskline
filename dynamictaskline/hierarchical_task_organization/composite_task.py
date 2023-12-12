# hierarchical_task_organization/composite_task.py

class CompositeTask:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.status = "Initialized"

    def add(self, task):
        self.children.append(task)

    def remove(self, task):
        self.children.remove(task)

    def execute(self):
        print(f"Starting '{self.name}'...")
        for child in self.children:
            child.execute()
        print(f"Finished '{self.name}'.")
