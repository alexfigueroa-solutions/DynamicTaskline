from rich.console import Console
from rich.tree import Tree
from rich.live import Live
from rich.layout import Layout
from rich.progress import (
    Progress,
    Task as ProgressTask,
    BarColumn,
    MofNCompleteColumn,
    TimeRemainingColumn,
    TextColumn
)
from rich.text import Text
import time
import subprocess


class FuturisticProgressBar(BarColumn):
    def render(self, task: ProgressTask) -> Text:
        completed = task.completed
        total = task.total
        width = self.max_width or 40
        bar_width = int(completed / total * width)
        pulse_width = int(time.monotonic() % 2 * width)  # Pulsing effect width

        # Create the bar style
        bar = "█" * bar_width
        pulse = "▒" * pulse_width
        remaining_bar = "░" * (width - bar_width - pulse_width)

        # Combine parts with pulsing effect
        full_bar = bar + (pulse if bar_width < width else '') + remaining_bar
        percentage = f"{task.percentage:>3.0f}%"

        # Create a text renderable with the bar and the percentage
        return Text(full_bar + " " + percentage, style="progress.bar.complete")

tree = Tree("Tasks")
console = Console()
progress = Progress(
    "[progress.description]{task.description}",
    FuturisticProgressBar(),
    "[progress.percentage]{task.percentage:>3.0f}%",
    TextColumn("[bold]{task.fields[bar]}"),
    TimeRemainingColumn(),
    expand=True
)
live = Live(console=console)

layout = Layout()



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
            return f"[red]ERROR: {self.error}[/red]"
        progress_int = int(self.progress)
        completed = "█" * (progress_int // 10)
        remaining = "░" * (10 - (progress_int // 10))
        percentage = f"{progress_int}%"
        return f"{completed}{remaining} {percentage}"

    def run_function(self, live, layout, root_task):
        if self.function:
            try:
                self.function(self, live, layout, root_task)
            except Exception as e:
                self.error = str(e)
                console.log(f"Error in {self.name}: {self.error}", style="bold red")  # Log error to console
                self.progress = 100  # Set to 100% to indicate the task has ended (with an error).


def do_work(task, live):
    for i in range(5):
        task.progress += 20
        task.update_progress()
        update_live_display(live, layout, root_task)
        time.sleep(1)  # Simulate work taking time
        task.tree_branch.add(f"{task.name} is working...")  # Add progress to the task's tree branch

    task.complete_task()

def run_os_command(task, live):
    try:
        result = subprocess.run(['echo', 'Hello World'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        task.complete_task()
        task.tree_branch.add(f"{task.name} command output: {result.stdout.decode().strip()}")  # Add output to the tree
    except subprocess.CalledProcessError as e:
        task.error = f"Command '{e.cmd}' returned non-zero exit status {e.returncode}."
        console.log(f"Error in {task.name}: {task.error}\n{e.stderr.decode()}", style="bold red")  # Log detailed error


def get_root_task_after_population():
    root_task = Task("Root Task", is_composite=True)
    child_task1 = Task("Child Task 1", do_work, is_composite=False)
    child_task2 = Task("Child Task 2", run_os_command, is_composite=False)
    child_task3 = Task("Child Task 3", is_composite=True)

    child_task1.add_child(Task("Subtask 1-1", do_work))
    child_task1.add_child(Task("Subtask 1-2", do_work))
    child_task3.add_child(Task("Subtask 3-1", do_work))
    child_task3.add_child(Task("Subtask 3-2", do_work))

    root_task.add_child(child_task1)
    root_task.add_child(child_task2)
    root_task.add_child(child_task3)

    return root_task

root_task = get_root_task_after_population()

def build_tree_with_progress(node, parent_tree):
    status = "✅" if node.is_complete() else "🕒"
    if node.error:
        status = "[red]❌[/red]"
    if not node.tree_branch:  # Initialize the tree branch if it does not exist.
        node.tree_branch = parent_tree.add(f"{status} {node.name} {node.get_progress_bar()}", guide_style="bold bright_blue")
    else:  # Update the tree branch if it exists.
        node.tree_branch.label = f"{status} {node.name} {node.get_progress_bar()}"
    for child in node.children:
        build_tree_with_progress(child, node.tree_branch)


def update_live_display(live, tree, root_task):
    build_tree_with_progress(root_task, tree)
    live.update(layout)

layout.split_column(
    Layout(name='tree_section', renderable=tree, size=20),
    Layout(name='progress_section', renderable=progress)
)

progress.start()

# Running tasks in sequence for demo purposes; in a real scenario, you might want to run these concurrently.
for task in root_task.children:
    task.run_function(live, layout, root_task)

def update_live_display(live, tree, root_task):
    build_tree_with_progress(root_task, tree)
    live.update(layout)

with Live(layout, console=console) as live:
    layout = Layout()
    # Bind the tree object to the layout
    layout.split_column(
        Layout(name='tree_section', renderable=tree, size=20),
        Layout(name='progress_section', renderable=progress)
    )
    progress.start()
    for task in root_task.children:
        task.run_function(live)  # Pass the live argument only
        update_live_display(live, tree, root_task)
    progress.stop()

console.log("[bold green]All tasks completed![/]")
