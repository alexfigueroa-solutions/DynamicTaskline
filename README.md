# DynamicTaskLine (Pre-Release)

**DynamicTaskLine** is a Python library designed to elevate command-line interfaces (CLI) into dynamic, structured, and responsive environments. It is tailored for developers looking to streamline complex workflows by organizing tasks in a hierarchical manner, providing real-time feedback, and presenting errors and logs contextually within each task level.

## Description

Traditionally, CLIs offer limited feedback during execution, making it difficult to manage complex tasks. **DynamicTaskLine** introduces a hierarchical, real-time task management system, transforming the CLI into an interactive workspace akin to a textual user interface (TUI). This approach not only enhances user experience but also provides a clear, searchable, and nested display of tasks, subtasks, informational messages, and errors.

## Features

- **Hierarchical Task Management**: Organize tasks into a parent-child relationship, mirroring the structure of your workflow with precision.
- **Real-Time Feedback**: Display the status of tasks as they happen, with immediate updates and progress indicators.
- **Contextual Information and Errors**: Keep all related information and errors neatly nested within each task, ensuring that logs are easy to follow and diagnose.
- **Interactive Configuration**: Adapt and configure tasks in real-time based on user input, making for a flexible and responsive CLI experience.
- **Nested CLI Outputs**: Each task or subtask maintains its output within its designated context, preserving a clean and structured interface.

## Getting Started

To install DynamicTaskLine and improve your CLI tools, run:

```sh
pip install dynamictaskline
```

### Prerequisites

Make sure you have Python 3.7 or later installed.

### Installing

You can easily install **DynamicTaskLine** using pip:

```sh
pip install dynamictaskline
```

## Usage

Here's a basic example to demonstrate a nested task structure with DynamicTaskLine:

```python
from dynamictaskline import TaskManager, Task

# Initialize the TaskManager
manager = TaskManager()

# Define a main task with a function
@manager.task(title="Main Task")
def main_task(data):
    # Your main task logic here
    return "Result of Main Task"

# Define a nested subtask
@manager.task(title="Sub Task", parent="Main Task")
def sub_task(data):
    # Your subtask logic, using data from the main task
    print(f"Handling subtask with data: {data}")

# Execute the task manager
manager.run()
```

## Documentation

For more details on the full capabilities of **DynamicTaskLine**, please refer to the [Documentation](#). It provides comprehensive guidelines on implementing the advanced features of DynamicTaskLine.

## Contributing

We welcome contributions to make **DynamicTaskLine** even better! Here's how you can help:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourAmazingFeature`)
3. Commit your Changes (`git commit -m 'Add YourAmazingFeature'`)
4. Push to the Branch (`git push origin feature/YourAmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` file for more information.
