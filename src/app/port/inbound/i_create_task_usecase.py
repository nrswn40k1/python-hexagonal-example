from abc import ABC, abstractmethod
from typing import Literal

from pydantic import BaseModel

from src.app.domain.model.task import Task


class CreateTaskRequest(BaseModel):
    title: str


class CreateTaskResponse(BaseModel):
    task: Task


class FailedToCreateTask(BaseModel):
    error_type: Literal["unknown"]
    error_msg: str = ""


class ICreateTaskUsecase(ABC):
    @abstractmethod
    def run(
        self, request: CreateTaskRequest
    ) -> CreateTaskResponse | FailedToCreateTask:
        pass
