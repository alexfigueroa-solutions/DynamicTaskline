# Contextual Information and Errors Feature for DynamicTaskLine

The **Contextual Information and Errors** feature is an integral part of the **DynamicTaskLine** library, designed to manage and display logs, errors, and informational messages within the appropriate task context. This feature enhances the ability to debug and understand the flow of complex processes by maintaining a clean and organized log structure.

## Architectural Overview

The implementation of contextual information and errors requires a logging system that understands the hierarchical task structure of **DynamicTaskLine**. Each task or subtask will have its logging context, capturing and displaying information relevant to its scope.

### Key Components

- **Log Context Manager**: Manages the creation and handling of log contexts for each task.
- **Error Handler**: Captures and formats exceptions and errors to be displayed within the task context.
- **Informational Logger**: Provides an API for tasks to log messages at various severity levels, maintaining task scope.

### Classes and Functions

- **`LogContext`**: A class representing a logging context for a task, managing messages and errors.
- **`ContextualLogger`**: Extends standard logging capabilities to maintain task context.

## Implementation Details

The feature will be built on top of Python's logging module, extending it to support task contexts. Here’s an illustrative implementation snippet:

```python
import logging
from dynamictaskline import TaskManager, Task
from dynamictaskline.logging import LogContext, ContextualLogger

# Initialize the TaskManager
manager = TaskManager()

# Configure the global logger to use ContextualLogger
logging.setLoggerClass(ContextualLogger)

@manager.task(title="Main Task")
def main_task(log: LogContext):
    log.info("Starting main task")

    try:
        # Main task logic
        log.info("Main task completed successfully")
    except Exception as e:
        log.error(f"An error occurred: {e}", exc_info=True)

@manager.task(title="Sub Task", parent="Main Task")
def sub_task(log: LogContext):
    log.info("Starting subtask")

    try:
        # Subtask logic
        log.info("Subtask completed successfully")
    except Exception as e:
        log.error(f"An error occurred in subtask: {e}", exc_info=True)

# Run the TaskManager
manager.run()
```

## Testing Scenarios

Testing will involve verifying that:

- Log messages and errors appear under the correct task in the output.
- The log context is properly passed down to subtasks.
- Errors are formatted and displayed according to the specifications.

Unit tests will use mock loggers and contexts to ensure messages are routed correctly, while integration tests will run sample tasks to check the real-world behavior of logging in a multi-level task environment.

## Documentation and Best Practices

Comprehensive documentation will be provided for developers to understand how to utilize the logging features effectively. This includes:

- Configuration of log levels.
- Formatting and filtering log messages.
- Best practices for error handling within tasks.

## Contribution Guidelines

As with other features, contributions that enhance the clarity, performance, and capabilities of the logging system will be encouraged. The contribution process will follow the standard workflow of forking, feature branching, and pull requests.
