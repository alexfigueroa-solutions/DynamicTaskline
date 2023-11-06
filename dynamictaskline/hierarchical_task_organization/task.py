import sys
import time

class Task:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.status = "Pending"

    def add_child(self, child_task):
        self.children.append(child_task)

    def execute(self):
        self.update_status("Running")
        for child in self.children:
            child.execute()
        self.update_status("Completed")

    def update_status(self, status):
        self.status = status
        self.display_status()
        time.sleep(1)  # Simulate task duration

    def display_status(self):
        indent = '  ' * self.get_level()
        sys.stdout.write(f"\r{indent}{self.status}: {self.name}")
        sys.stdout.flush()

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def run(self):
        try:
            self.execute()
        except Exception as e:
            self.update_status("Error")
            print(f"\n{self.get_level() * '  '}Error Details: {e}")
