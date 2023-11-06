from rich.console import Console
from rich.tree import Tree
from rich.live import Live
import time

class Task:
    def __init__(self, name, is_composite=False):
        self.name = name
        self.progress = 0
        self.children = []
        self.completed = False
        self.is_composite = is_composite

    def add_child(self, task):
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
        progress_int = int(self.progress)
        completed = "█" * (progress_int // 10)
        remaining = "░" * (10 - (progress_int // 10))
        percentage = f"{progress_int}%"
        return f"{completed}{remaining} {percentage}"

def build_tree_with_progress(node, parent_tree):
    status = "✅" if node.is_complete() else "🕒"
    branch = parent_tree.add(f"{status} {node.name} {node.get_progress_bar()}")
    for child in node.children:
        build_tree_with_progress(child, branch)

root_task = Task("Root", is_composite=True)
composite_task = Task("CompositeTask", is_composite=True)
leaf_task1 = Task("LeafTask1")
leaf_task2 = Task("LeafTask2")
leaf_task3 = Task("LeafTask3")

composite_task.add_child(leaf_task1)
composite_task.add_child(leaf_task2)
composite_task.add_child(leaf_task3)
root_task.add_child(composite_task)

console = Console()

def simulate_task_progress(task, increment=10):
    if not task.is_complete():
        task.progress += increment
        if task.progress >= 100:
            task.complete_task()
        task.update_progress()

console = Console()

with Live(console=console, refresh_per_second=10) as live:
    while not root_task.is_complete():
        tree = Tree(":gear: Running Tasks")
        build_tree_with_progress(root_task, tree)
        live.update(tree)

        # Update progress for each task one by one
        for task in composite_task.children:
            if not task.is_complete():
                simulate_task_progress(task)
                break  # Break after updating one task to update the display

        # Update progress for composite and root tasks after changes in children
        composite_task.update_progress()
        root_task.update_progress()

        time.sleep(1)  # Sleep to simulate time for the task progress

final_tree = Tree(":checkered_flag: All tasks completed")
build_tree_with_progress(root_task, final_tree)
console.print(final_tree)
