from enum import Enum
from uuid import uuid4

from pydantic import BaseModel, Field, field_serializer


class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class Task(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), frozen=True)
    title: str
    status: TaskStatus = Field(default=TaskStatus.TODO)

    @classmethod
    def create(cls, title: str) -> "Task":
        return cls(title=title)

    def progress_status(self) -> None:
        if self.status == TaskStatus.TODO:
            self.status = TaskStatus.IN_PROGRESS
        elif self.status == TaskStatus.IN_PROGRESS:
            self.status = TaskStatus.DONE
        return

    @field_serializer("status")
    def serialize_status(self, status: TaskStatus) -> str:
        return status.value
