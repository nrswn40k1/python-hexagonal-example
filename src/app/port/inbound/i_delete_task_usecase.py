from abc import ABC, abstractmethod
from typing import Literal

from pydantic import BaseModel


class DeleteTaskRequest(BaseModel):
    task_id: str


class DeleteTaskResponse(BaseModel):
    success: bool = True


class FailedToDeleteTask(BaseModel):
    error_type: Literal["task_not_found", "unknown"]
    error_msg: str = ""


class IDeleteTaskUsecase(ABC):
    @abstractmethod
    def run(
        self, request: DeleteTaskRequest
    ) -> DeleteTaskResponse | FailedToDeleteTask:
        pass
