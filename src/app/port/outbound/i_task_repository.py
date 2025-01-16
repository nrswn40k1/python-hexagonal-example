from abc import ABC, abstractmethod

from src.app.domain.task import Task


class ITaskRepository(ABC):
    @abstractmethod
    def load_by_id(self, task_id: str) -> Task:
        pass

    @abstractmethod
    def load_all(self) -> list[Task]:
        pass

    @abstractmethod
    def add(self, task: Task) -> None:
        pass

    @abstractmethod
    def update(self, task: Task) -> None:
        pass

    @abstractmethod
    def delete(self, task_id: str) -> None:
        pass
