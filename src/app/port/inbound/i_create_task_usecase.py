from abc import ABC, abstractmethod
from typing import Literal

from pydantic import BaseModel

from src.app.domain.task import Task


class CreateTaskRequest(BaseModel):
    title: str


class CreateTaskResponse(BaseModel):
    id: str
    title: str
    status: Literal["todo", "in_progress", "done"]

    @classmethod
    def create(cls, task: Task) -> "CreateTaskResponse":
        return cls(id=task.id, title=task.title, status=task.status.value)


class FailedToCreateTask(BaseModel):
    error_type: Literal["unknown"]
    error_msg: str = ""


class ICreateTaskUsecase(ABC):
    @abstractmethod
    def run(
        self, request: CreateTaskRequest
    ) -> CreateTaskResponse | FailedToCreateTask:
        pass
