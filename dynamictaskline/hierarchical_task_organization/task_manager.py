from rich.console import Console
from rich.progress import Progress, TaskID
import time

class TaskManager:
    def __init__(self):
        self.console = Console()
        self.progress = Progress()

    def add_task(self, description: str, total: int = 100) -> TaskID:
        task_id = self.progress.add_task(description, total=total)
        return task_id

    def update_task(self, task_id: TaskID, advance: int):
        self.progress.update(task_id, advance=advance)

    def run(self, task_descriptions):
        with self.progress:
            task_ids = {desc: self.add_task(f"Running: {desc}") for desc in task_descriptions}

            while not self.progress.finished:
                # In a real application, you would call update_task as needed
                # For demonstration, we'll simulate some work with sleep and update
                for desc, task_id in task_ids.items():
                    time.sleep(1)  # Simulate work
                    self.update_task(task_id, advance=10)
                    if self.progress.tasks[task_id].completed:
                        break  # Exit if the task is completed
