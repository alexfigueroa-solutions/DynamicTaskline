from .task_manager import TaskManager
from .ui_renderer import render

def main():
    manager = TaskManager()

    # Render the initial UI
    render("Welcome to DynamicTaskLine CLI")

    # Example task
    manager.add_task("Initialize Project")
    manager.add_subtask("Initialize Project", "Setup Virtual Environment")

    # Run tasks
    manager.run_all()
