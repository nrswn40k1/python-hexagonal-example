from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.app.domain.model.task import Task


class CreateTaskRequest(BaseModel):
    title: str


class CreateTaskResponse(BaseModel):
    task: Task


class ICreateTaskUsecase(ABC):
    @abstractmethod
    def run(self, request: CreateTaskRequest) -> CreateTaskResponse:
        pass
