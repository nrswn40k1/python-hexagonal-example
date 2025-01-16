from abc import ABC, abstractmethod
from typing import Literal

from pydantic import BaseModel


class DeleteTaskRequest(BaseModel):
    task_id: str


class DeleteTaskResponse(BaseModel):
    success: bool = True


class FailedToDeleteTask(Exception):
    def __init__(
        self, error_type: Literal["task_not_found", "unknown"], error_msg: str
    ):
        self.error_type = error_type
        super().__init__(error_msg)


class IDeleteTaskUsecase(ABC):
    @abstractmethod
    def run(self, request: DeleteTaskRequest) -> DeleteTaskResponse:
        pass
