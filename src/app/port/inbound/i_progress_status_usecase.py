from abc import ABC, abstractmethod
from typing import Literal

from pydantic import BaseModel

from src.app.domain.model.task import Task


class ProgressStatusRequest(BaseModel):
    task_id: str


class ProgressStatusResponse(BaseModel):
    task: Task


class FailedToProgressStatus(BaseModel):
    error_type: Literal["task_not_found", "unknown"]
    error_msg: str = ""


class IProgressStatusUsecase(ABC):
    @abstractmethod
    def run(
        self, request: ProgressStatusRequest
    ) -> ProgressStatusResponse | FailedToProgressStatus:
        pass
