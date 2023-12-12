import sys
import time

class Task:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.status = "Pending"
        self.indentation = '  ' * self.get_level()

    def add_child(self, child_task):
        self.children.append(child_task)

    def execute(self):
        self.update_status("Running")
        for child in self.children:
            child.execute()
        self.update_status("Completed")
        if self.parent:
            self.parent.collapse_children()

    def update_status(self, status):
        self.status = status
        self.display_status()
        time.sleep(0.5)  # Simulate task duration

    def display_status(self):
        sys.stdout.write(f"\r{self.indentation}{self.status}: {self.name}\n")
        sys.stdout.flush()

    def collapse_children(self):
        if all(child.status == "Completed" for child in self.children):
            self.move_cursor_up(len(self.children))
            self.display_status()

    def move_cursor_up(self, lines):
        sys.stdout.write(f"\033[{lines}A")
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
            print(f"{self.indentation}Error Details: {e}")
