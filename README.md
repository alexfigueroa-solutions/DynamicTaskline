# DynamicTaskLine

**DynamicTaskLine** is a Python library that brings real-time task management and a dynamic user interface to command-line applications. It provides developers with the tools to create structured, responsive, and interactive CLI workflows, supporting nested task execution, dynamic status updates, and seamless data propagation.

## Description

Command-line interfaces (CLI) are powerful tools for system administration, development workflows, and automation scripts. However, building CLIs that handle complex, multi-level tasks in real time can be challenging. DynamicTaskLine simplifies this by introducing a structured approach to task management within your command-line applications. By incorporating real-time feedback and hierarchical task execution, this library enables developers and users alike to monitor and control processes more efficiently and effectively.

## Features

- **Hierarchical Task Organization:** Craft your CLI with main tasks and nested subtasks to improve management and clarity.
- **Dynamic Status Updates:** Monitor the progress of tasks in real time with live status updates.
- **Data Propagation:** Ensure that output data from tasks flows seamlessly to subsequent tasks.
- **Interactive Configuration:** Directly configure projects via the CLI, adapting task execution on-the-fly according to user inputs.
- **Nested CLI Outputs**: Ensure that the output from each task or subtask is rendered within its own CLI context, maintaining a clean and organized display of information. This feature emphasizes the hierarchical nature of tasks by visually nesting the outputs to reflect the structure.

## Getting Started

To get started with DynamicTaskLine, install the package via `pip`:

```bash
pip install dynamictaskline
```

### Prerequisites

DynamicTaskLine requires Python 3.7 or newer.

### Installing

Install DynamicTaskLine using pip:

```bash
pip install dynamictaskline
```

## Usage

Here is a simple example to illustrate the setup of a DynamicTaskLine workflow:

```python
from dynamictaskline import TaskManager, Task

# Initialize TaskManager
manager = TaskManager()

# Define a main task with a sample function
@manager.task(title="Main Task")
def main_task(data):
    # Task logic goes here
    return "Result of Main Task"

# Define a subtask
@manager.task(title="Sub Task", parent="Main Task")
def sub_task(data):
    # Subtask logic utilizing data from the main task
    print(f"Processing subtask with data: {data}")

# Run the task manager
manager.run()
```

### Documentation

Please refer to the [Documentation](https://github.com/username/dynamictaskline/wiki) for detailed information on how to implement and utilize all the features provided by DynamicTaskLine.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.
