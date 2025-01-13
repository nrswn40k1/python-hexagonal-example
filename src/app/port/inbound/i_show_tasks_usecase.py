from abc import ABC, abstractmethod
from typing import Literal

from pydantic import BaseModel

from src.app.domain.model.task import Task


class ShowTasksResponse(BaseModel):
    tasks: list[Task]


class FailedToShowTasks(BaseModel):
    error_type: Literal["unknown"]
    error_msg: str = ""


class IShowTasksUsecase(ABC):
    @abstractmethod
    def run(self) -> ShowTasksResponse | FailedToShowTasks:
        pass
