from dynamictaskline.hierarchical_task_organization.task_manager import TaskManager
from dynamictaskline.hierarchical_task_organization.leaf_task import LeafTask
from dynamictaskline.contextual_info.info_logger import InfoLogger

def simple_task_action():
    logger = InfoLogger("SimpleWorkflow")
    logger.log("This is a simple task action being executed.")

def main():
    task_manager = TaskManager()
    simple_task = LeafTask("SimpleTask", simple_task_action)
    task_manager.add_task(simple_task)
    task_manager.execute()

if __name__ == "__main__":
    main()
