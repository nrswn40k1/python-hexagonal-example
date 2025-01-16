from abc import ABC, abstractmethod
from typing import Literal

from pydantic import BaseModel

from src.app.domain.task import Task


class TaskDto(BaseModel):
    id: str
    title: str
    status: Literal["todo", "in_progress", "done"]

    @classmethod
    def create(cls, task: Task) -> "TaskDto":
        return cls(id=task.id, title=task.title, status=task.status.value)


class ShowTasksResponse(BaseModel):
    tasks: list[TaskDto]

    @classmethod
    def create(cls, tasks: list[Task]) -> "ShowTasksResponse":
        return cls(tasks=[TaskDto.create(task) for task in tasks])


class FailedToShowTasks(BaseModel):
    error_type: Literal["unknown"]
    error_msg: str = ""


class IShowTasksUsecase(ABC):
    @abstractmethod
    def run(self) -> ShowTasksResponse | FailedToShowTasks:
        pass
