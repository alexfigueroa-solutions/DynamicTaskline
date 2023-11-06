from dynamictaskline.hierarchical_task_organization.task_manager import TaskManager
from dynamictaskline.hierarchical_task_organization.composite_task import CompositeTask
from dynamictaskline.hierarchical_task_organization.leaf_task import LeafTask
from dynamictaskline.real_time_feedback.output_stream_manager import OutputStreamManager
from dynamictaskline.real_time_feedback.status_renderer import StatusRenderer
from dynamictaskline.real_time_feedback.feedback_controller import FeedbackController
from dynamictaskline.contextual_info.log_context_manager import LogContextManager
from dynamictaskline.contextual_info.contextual_logger import ContextualLogger
from dynamictaskline.hierarchical_task_organization.task import Task

def main():
    # Contextual logging setup
    context_manager = LogContextManager()
    logger = ContextualLogger("DynamicTaskLine", context_manager)

    # Real-time feedback setup
    output_stream_manager = OutputStreamManager()
    status_renderer = StatusRenderer(output_stream_manager)
    feedback_controller = FeedbackController(status_renderer)

    manager = TaskManager()

    # Create tasks
    composite_task = Task("CompositeTask")
    leaf_task1 = Task("LeafTask1", composite_task)
    leaf_task2 = Task("LeafTask2", composite_task)

    # Add tasks to the manager
    manager.add_task(composite_task)
    manager.add_task(leaf_task1, composite_task)
    manager.add_task(leaf_task2, composite_task)

    # Run the task manager
    manager.run()

    # Provide feedback
    feedback_controller.provide_feedback("All tasks executed.")

if __name__ == "__main__":
    main()
