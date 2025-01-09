from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.app.domain.model.task import Task


class ShowTasksResponse(BaseModel):
    tasks: list[Task]


class IShowTasksUsecase(ABC):
    @abstractmethod
    def run(self) -> ShowTasksResponse:
        pass
