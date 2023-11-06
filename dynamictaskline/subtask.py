class Subtask:
    def __init__(self, title):
        self.title = title
        self.status = "Not Started"

    def run(self):
        self.status = "In Progress"
        # Simulating subtask execution
        print(f"Subtask '{self.title}' is {self.status}.")
        # Here, you would add actual functionality
        self.status = "Completed"
        print(f"Subtask '{self.title}' is {self.status}.")
