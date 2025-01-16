from src.app.domain.exceptions import TaskNotFoundException
from src.app.domain.task import Task
from src.app.port.outbound.i_task_repository import ITaskRepository


class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self._tasks: dict[str, Task] = {}

    def load_by_id(self, task_id: str) -> Task:
        if task_id not in self._tasks:
            raise TaskNotFoundException(task_id)
        return self._tasks[task_id]

    def load_all(self) -> list[Task]:
        return list(self._tasks.values())

    def add(self, task: Task) -> None:
        if task.id in self._tasks:
            raise ValueError("Task already exists")
        self._tasks[task.id] = task

    def update(self, task: Task) -> None:
        if task.id not in self._tasks:
            raise TaskNotFoundException(task.id)
        self._tasks[task.id] = task

    def delete(self, task_id: str) -> None:
        if task_id not in self._tasks:
            raise TaskNotFoundException(task_id)
        del self._tasks[task_id]
