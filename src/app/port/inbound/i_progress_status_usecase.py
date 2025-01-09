from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.app.domain.model.task import Task


class ProgressStatusRequest(BaseModel):
    task_id: str


class ProgressStatusResponse(BaseModel):
    task: Task


class IProgressStatusUsecase(ABC):
    @abstractmethod
    def run(self, request: ProgressStatusRequest) -> ProgressStatusResponse:
        pass
