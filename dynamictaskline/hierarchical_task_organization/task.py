class Task:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.status = "Pending"

    def add_child(self, child_task):
        self.children.append(child_task)

    def execute(self):
        self.start_task()
        for child in self.children:
            child.execute()
        self.complete_task()

    def start_task(self):
        self.status = "Running"
        self.display_status()

    def complete_task(self):
        self.status = "Completed"
        self.display_status()

    def display_status(self):
        indent = '  ' * self.get_level()
        print(f"{indent}{self.status}: {self.name}")

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
            self.handle_error(e)

    def handle_error(self, error):
        self.status = "Error"
        self.display_status()
        print(f"{self.get_level() * '  '}Error Details: {error}")
