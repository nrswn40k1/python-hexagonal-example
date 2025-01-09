import os

CONTROLLER_TYPE: str = os.getenv("CONTROLLER_TYPE", "cli")
TASK_REPOSITORY_TYPE: str = os.getenv("TASK_REPOSITORY_TYPE", "inmemory")
