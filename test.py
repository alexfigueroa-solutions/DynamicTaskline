from rich.console import Console
from rich.tree import Tree
from rich.live import Live
import time
import subprocess

class Task:
    def __init__(self, name, function=None, is_composite=False):
        self.name = name
        self.progress = 0
        self.children = []
        self.completed = False
        self.is_composite = is_composite
        self.function = function
        self.error = None
        self.tree_branch = None

    def add_child(self, task):
        if self.is_composite:
            self.children.append(task)

    def is_complete(self):
        if self.is_composite:
            self.completed = all(child.is_complete() for child in self.children)
        return self.completed

    def complete_task(self):
        self.completed = True
        self.progress = 100

    def update_progress(self):
        if self.is_composite:
            self.progress = sum(child.progress for child in self.children) // len(self.children)

    def get_progress_bar(self):
        if self.error:
            return f"[red]ERROR[/red]"
        progress_int = int(self.progress)
        completed = "█" * (progress_int // 10)
        remaining = "░" * (10 - (progress_int // 10))
        percentage = f"{progress_int}%"
        return f"{completed}{remaining} {percentage}"

    def run_function(self, live):
        if self.function:
            try:
                self.function(self, live)
            except Exception as e:
                self.error = str(e)
                self.progress = 100  # Set to 100% to indicate the task has ended (with an error).

# This function now checks if the tree branch exists before creating it.
def build_tree_with_progress(node, parent_tree):
    status = "✅" if node.is_complete() else "🕒"
    if node.error:
        status = "[red]❌[/red]"
    if not node.tree_branch:  # Initialize the tree branch if it does not exist.
        node.tree_branch = parent_tree.add(f"{status} {node.name} {node.get_progress_bar()}")
    else:  # Update the tree branch if it exists.
        node.tree_branch.label = f"{status} {node.name} {node.get_progress_bar()}"
    for child in node.children:
        build_tree_with_progress(child, node.tree_branch)

# Define some real functions to do work
def do_work(task, live):
    for i in range(5):
        task.progress += 20
        task.update_progress()
        update_live_display(live)
        time.sleep(1)  # Simulate work taking time
        task.tree_branch.add(f"{task.name} is working...")  # Add progress to the task's tree branch

    task.complete_task()

def run_os_command(task, live):
    try:
        result = subprocess.run(['echo', 'Hello World'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        task.complete_task()
        task.tree_branch.add(f"{task.name} command output: {result.stdout.decode().strip()}")  # Add output to the tree
    except subprocess.CalledProcessError as e:
        task.error = str(e)
    task.progress = 100
    update_live_display(live)

def update_live_display(live):
    if not root_task.tree_branch:
        tree = Tree(":gear: Running Tasks")
        build_tree_with_progress(root_task, tree)
        live.update(tree)
    else:
        build_tree_with_progress(root_task, root_task.tree_branch)

# Create tasks with actual functions to run
root_task = Task("Root", is_composite=True)
composite_task = Task("CompositeTask", is_composite=True)
leaf_task1 = Task("LeafTask1", function=do_work)
leaf_task2 = Task("LeafTask2", function=do_work)
leaf_task3 = Task("LeafTask3", function=run_os_command)

# Set up the task hierarchy
composite_task.add_child(leaf_task1)
composite_task.add_child(leaf_task2)
composite_task.add_child(leaf_task3)
root_task.add_child(composite_task)

console = Console()

def simulate_task_progress(task, live):
    if task.is_composite:
        for child in task.children:
            simulate_task_progress(child, live)
    else:
        task.run_function(live)

    task.update_progress()
    update_live_display(live)

with Live(console=console, refresh_per_second=10) as live:
    simulate_task_progress(root_task, live)  # Start with the root task

    while not root_task.is_complete():
        update_live_display(live)
        time.sleep(0.5)  # A short sleep to prevent a busy-wait loop

    # Final update to ensure the last task's completion is displayed
    update_live_display(live)
