from abc import ABC, abstractmethod
from typing import Literal

from pydantic import BaseModel


class DeleteTaskRequest(BaseModel):
    task_id: str


class DeleteTaskResponse(BaseModel):
    result: Literal["success", "failure"]


class IDeleteTaskUsecase(ABC):
    @abstractmethod
    def run(self, request: DeleteTaskRequest) -> DeleteTaskResponse:
        pass
