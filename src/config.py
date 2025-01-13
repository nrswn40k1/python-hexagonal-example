import os

CONTROLLER_TYPE: str = os.getenv("CONTROLLER_TYPE", "fastapi")
TASK_REPOSITORY_TYPE: str = os.getenv("TASK_REPOSITORY_TYPE", "inmemory")
PORT = int(os.getenv("PORT", 8000))
HOST = os.getenv("HOST", "0.0.0.0")
